# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PySide6-Template is a Qt6-based GUI application template for creating desktop applications, including a QR code generation example. The project follows a Qt Designer workflow where UI files (.ui) are compiled to Python code using pyside6-uic.

## Development Workflow

### Key Commands

**Start Qt Designer** (Windows)
```
designer.bat
```
Or directly:
```
pyside6-designer src/ui/Ui_MainWindow.ui
```

**Compile UI files** (generate Python from .ui files)
```
pyside6-uic src/ui/Ui_MainWindow.ui > src/ui/Ui_MainWindow.py
```
Windows batch wrapper:
```
uicAll.bat
```

**Run the application**
```
python src/template.py
```

**Build executable** (PyInstaller)
```
python auto_build.py
```
Windows batch wrapper:
```
build.bat
```

### Project Dependencies

- **PySide6** (>=6.4.0): Core GUI framework
- **pyqt6-tools** (optional): Provides Qt Designer and other tools
- **build, wheel**: For packaging
- **PyInstaller**: For building standalone executables

Install development environment:
```
pip install -e .
pip install -e ".[dev]"
```

## Project Structure

```
src/
├── template.py              # Main application entry point
├── ui/
│   ├── Ui_MainWindow.ui    # Qt Designer UI file
│   └── Ui_MainWindow.py    # Generated from .ui file (DO NOT edit directly)
├── css/                     # Stylesheets (CSS)
│   ├── buttons/            # Button-specific styles
│   └── *.css
└── assets/                  # Application images and icons

auto_build.py               # PyInstaller build script with venv detection
pyrightconfig.json          # Pyright type checking config (disabled)
setup.cfg                   # Flake8, pylint, mypy configuration
```

## Important Development Notes

### UI File Workflow

1. **Edit UI in Qt Designer**: Open `Ui_MainWindow.ui` with `pyside6-designer`
2. **Compile to Python**: Run `pyside6-uic src/ui/Ui_MainWindow.ui > src/ui/Ui_MainWindow.py`
3. **Use in Application**: Import `Ui_MainWindow` in your main window class and call `self.ui.setupUi(self)`

**DO NOT** manually edit `Ui_MainWindow.py` — it will be overwritten when recompiling the .ui file.

### Stylesheet Loading

The main window loads CSS stylesheets from the `src/css/` directory via the `load_stylesheet()` method. Default stylesheet is `styles.css`. CSS files are loaded relative to the `src` directory.

### Known Issues / In Progress

From README:
- Central widget layout management needs work (RM > Layout)
- Global CSS styling implementation pending

### Type Checking

Pyright is configured but disabled (`typeCheckingMode: "off"`). Main module source checking is disabled (`reportMissingModuleSource: "none"`). PySide6 import warnings are suppressed.

### Code Style

Linting is configured via `setup.cfg`. Notable settings:
- Max line length: 160 characters
- Flake8 excludes generated UI files (`ui_*`)
- Pylint ignores generated UI files and test directories
- Wildcard imports are disabled for pylint

## Build System (PyInstaller)

The `auto_build.py` script:
- Detects virtual environment and warns if not in one
- Automatically includes critical packages (cv2, numpy, PyQt6, etc.)
- Includes all necessary data files (icons, UI, images)
- Builds to `dist/` directory
- Creates a one-directory bundle by default

Target entry point: `src/BookImagerQT.py` (may need updating for this template)
