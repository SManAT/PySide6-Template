#!/usr/bin/env python3
"""cx_Freeze build configuration for QTurtle"""

import sys
from pathlib import Path
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "PySide6.QtPrintSupport",
        "qrcode",
        "ui",
        "ui.Ui_MainWindow",
    ],
    "include_files": [
        ("src/qrcode_app/css", "lib/qrcode_app/css"),
        ("src/qrcode_app/ui/Ui_MainWindow.ui", "lib/qrcode_app/ui/Ui_MainWindow.ui"),
    ],
    "excludes": [
        "PyQt6",
        "matplotlib",
        "scipy",
        "numpy",
        "pandas",
        "PIL",
        "wx",
        "IPython",
        "jupyter",
        "notebook",
        "tkinter",
        "test",
        "unittest",
        "doctest",
        "pydoc",
        "xmlrpc",
        "ftplib",
        "poplib",
        "imaplib",
        "smtplib",
    ],
    "optimize": 2,
    "include_msvcr": True,
    "build_exe": "build/cxfreeze_temp",
}

icon_path = "assets/app.ico"

executables = [
    Executable(
        script="src/qrcode_app/__main__.py",
        base="gui" if sys.platform == "win32" else None,
        target_name="QRCode.exe" if sys.platform == "win32" else "QRCode",
        icon=icon_path if (sys.platform == "win32" and Path(icon_path).exists()) else None,
    )
]

setup(
    name="QRCode",
    version="1.0.0",
    description="Python IDE for turtle graphics scripts",
    options={"build_exe": build_exe_options},
    executables=executables,
)
