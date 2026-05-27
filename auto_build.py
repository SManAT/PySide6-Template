#!/usr/bin/env python3
"""Build script with pyproject.toml integration and virtual environment detection"""

import os
import sys
from pathlib import Path
from typing import List, Set

# Handle tomllib import for different Python versions
try:
    if sys.version_info >= (3, 11):
        import tomllib
    else:
        import tomli as tomllib
except ImportError:
    print("❌ Error: tomli is required for Python < 3.11")
    print("   Install with: pip install tomli")
    sys.exit(1)

import PyInstaller.__main__


def load_pyproject():
    """Load and parse pyproject.toml"""
    pyproject_path = Path("pyproject.toml")

    if not pyproject_path.exists():
        raise FileNotFoundError("pyproject.toml not found in current directory")

    try:
        with open(pyproject_path, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to parse pyproject.toml: {e}")


def check_virtual_env():
    """Check if running in virtual environment and show info"""
    in_venv = hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)

    venv_path = os.environ.get("VIRTUAL_ENV", None)

    print("=" * 60)
    print("Environment Check")
    print("=" * 60)
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Running in venv: {'✅ YES' if in_venv else '❌ NO'}")

    if venv_path:
        print(f"Virtual env path: {venv_path}")
    else:
        print("Using system Python installation")

    if not in_venv:
        print("\n⚠ WARNING: Not running in virtual environment!")

        venv_dir = Path(".venv")
        if venv_dir.exists():
            if sys.platform == "win32":
                print("   Recommendation: .venv\\Scripts\\activate")
            else:
                print("   Recommendation: source .venv/bin/activate")

    print("=" * 60 + "\n")


def get_installed_packages() -> Set[str]:
    """Get set of installed packages"""
    import pkg_resources

    return {pkg.key for pkg in pkg_resources.working_set}


def extract_package_names(dependencies: List[str]) -> Set[str]:
    """Extract package names from dependency specifications"""
    packages = set()
    for dep in dependencies:
        # Handle version specifiers and environment markers
        pkg_name = dep.split(";")[0]  # Remove markers
        pkg_name = pkg_name.split(">=")[0].split("==")[0].split("<")[0].split(">")[0].split("!")[0].strip()
        if pkg_name:
            packages.add(pkg_name.lower().replace("-", "_"))
    return packages


def get_hidden_imports(pyproject: dict) -> List[str]:
    """Generate hidden imports from pyproject.toml dependencies"""
    installed = get_installed_packages()

    # Collect all dependency names
    dependencies = set()

    # Main dependencies
    if "dependencies" in pyproject.get("project", {}):
        dependencies.update(extract_package_names(pyproject["project"]["dependencies"]))

    # Dev dependencies
    optional_deps = pyproject.get("project", {}).get("optional-dependencies", {})
    for opt_key, opt_deps in optional_deps.items():
        dependencies.update(extract_package_names(opt_deps))

    # Package name mappings (for cases where import name != package name)
    name_mappings = {
        "opencv-python": "cv2",
        "opencv-python-headless": "cv2",
        "pillow": "PIL",
        "pyyaml": "yaml",
        "scikit-learn": "sklearn",
        "beautifulsoup4": "bs4",
        "pyqt6": "PyQt6",
        "pyqt5": "PyQt5",
        "pyside6": "PySide6",
    }

    hidden_imports = []
    skip_packages = {"pip", "setuptools", "wheel", "pyinstaller", "build", "tomli", "tomllib", "pyqt6-tools"}

    for dep in sorted(dependencies):
        if dep in skip_packages:
            continue

        import_name = name_mappings.get(dep, dep.replace("-", "_"))

        if dep in installed or import_name.lower() in [p.replace("-", "_") for p in installed]:
            hidden_imports.append(import_name)

    return hidden_imports


def find_entry_point() -> str:
    """Find the main entry point script"""
    candidates = [
        "src/main.py",
        "src/app.py",
        "src/template.py",
        "src/BookImagerQT.py",
        "main.py",
        "app.py",
    ]

    for candidate in candidates:
        if Path(candidate).exists():
            return candidate

    raise FileNotFoundError("Could not find entry point. Tried: " + ", ".join(candidates))


def get_app_name(pyproject: dict) -> str:
    """Get application name from pyproject.toml"""
    name = pyproject.get("project", {}).get("name", "app").lower()
    return name.replace("_", "-").replace(" ", "-")


def get_data_files() -> List[tuple]:
    """Get list of data files to include based on what exists"""
    files = []

    data_mappings = [
        ("src/app.ico", "."),
        ("src/ui", "ui"),
        ("src/icons", "icons"),
        ("src/images", "images"),
        ("src/classes/logger_config.yaml", "classes"),
    ]

    for src, dest in data_mappings:
        if Path(src).exists():
            files.append((src, dest))

    return files


def build():
    """Build the application"""
    # Load configuration
    print("📄 Loading pyproject.toml...")
    pyproject = load_pyproject()

    app_name = get_app_name(pyproject)
    print(f"   App name: {app_name}")

    # Check environment
    check_virtual_env()

    # Find entry point
    print("🔍 Finding entry point...")
    entry_point = find_entry_point()
    print(f"   Using: {entry_point}")

    # Get hidden imports from dependencies
    print("\n📦 Detecting dependencies from pyproject.toml...")
    hidden_imports = get_hidden_imports(pyproject)
    print(f"   Found {len(hidden_imports)} packages")

    print("\n🔍 Key packages detected:")
    key_packages = ["cv2", "numpy", "PySide6", "PyQt6", "PIL", "qrcode"]
    for pkg in key_packages:
        if pkg in hidden_imports:
            print(f"   ✓ {pkg}")

    # Platform separator
    sep = ";" if sys.platform == "win32" else ":"

    # Build arguments
    args = [
        entry_point,
        "--windowed",
        f"--name={app_name}",
    ]

    # Add icon if it exists
    if Path("src/app.ico").exists():
        args.append("--icon=src/app.ico")

    # Add data files
    data_files = get_data_files()
    for src, dest in data_files:
        args.append(f"--add-data={src}{sep}{dest}")

    # Add standard options
    args.extend(
        [
            "--clean",
            "--noconfirm",
            "--onedir",
            "--console",
        ]
    )

    # Add all detected hidden imports
    for imp in hidden_imports:
        args.append(f"--hidden-import={imp}")

    # Add PySide6/PyQt6 specific imports (critical for Qt apps)
    qt_package = None
    if "PySide6" in hidden_imports:
        qt_package = "PySide6"
    elif "PyQt6" in hidden_imports:
        qt_package = "PyQt6"

    if qt_package:
        qt_modules = [f"{qt_package}.QtCore", f"{qt_package}.QtGui", f"{qt_package}.QtWidgets"]
        for mod in qt_modules:
            args.append(f"--hidden-import={mod}")
        args.append(f"--collect-all={qt_package}")

    # Collect all data for other critical packages
    for pkg in ["numpy", "cv2", "PIL"]:
        if pkg in hidden_imports:
            args.append(f"--collect-all={pkg}")

    print("\n🔨 Building with PyInstaller...")
    print(f"   Entry point: {entry_point}")
    print(f"   Output: dist/{app_name}/")
    print()

    PyInstaller.__main__.run(args)

    print("\n✅ Build complete!")
    print(f"   Executable: dist/{app_name}/")


if __name__ == "__main__":
    try:
        build()
    except KeyboardInterrupt:
        print("\n\n❌ Build cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Build failed: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
