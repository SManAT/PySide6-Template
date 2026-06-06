# PySide6-Template
A pyside 6 template for students, also included 

- Deployment Tools, PySide, Briefcase, cx_freeze and Nuktia see [PyInstaller.md](PyInstaller.md)

# Introduction

This template is an example application to create QR Codes. It explains the common workflow for beginners.
You will have for Windows some Batch Files. Those Batch Files are starting the pyside6 apps like designer or ui-compiler.

The application is generating a QR Code, that implements WLAN SSID and Password.

If you use it as Template, just delete the QRCode Parts and you are done.

Check also *pyproject.toml*, and correct the dependencies part.

```
dependencies = [
    "pyside6-essentials>=6.4.0",
    "qrcode",
    "pillow"
]
```

To setup all Py modules do

```
pip install -e .
```



# FIle Structure (important!)

```
src/
└── qrcode/              # Your package directory
    ├── __init__.py
    ├── ui/
    │   ├── __init__.py
    │   └── Ui_MainWindow.py
    └── __main__.py
```



## PySide 6 Applications

| Programm | Kurzbeschreibung |
|----------|------------------|
| `pyside6-uic` | Konvertiert Qt Designer UI-Dateien (.ui) in Python-Code |
| `pyside6-rcc` | Kompiliert Qt-Ressourcendateien (.qrc) in Python-Module |
| `pyside6-designer` | Startet Qt Designer für grafisches UI-Design |
| `pyside6-assistant` | Öffnet Qt Assistant für Dokumentation und Hilfe |
| `pyside6-linguist` | Übersetzungstool für Qt-Anwendungen (i18n/l10n) |
| `pyside6-lrelease` | Kompiliert Übersetzungsdateien (.ts) in binäre Formate (.qm) |
| `pyside6-lupdate` | Extrahiert übersetzbare Strings aus Quellcode in .ts-Dateien |
| `pyside6-qml` | Startet QML-Runtime für QML-Anwendungen |
| `pyside6-qmlls` | QML Language Server für IDE-Integration |
| `pyside6-qmltestrunner` | Führt QML-Tests aus |
| `pyside6-deploy` | Deployment-Tool für PySide6-Anwendungen |
| `pyside6-project` | Projektmanagement-Tool für PySide6-Entwicklung |
| `pyside6-genpyi` | Generiert Python-Stub-Dateien (.pyi) für Typisierung |
| `pyside6-metaobjectdump` | Analysiert Qt-MetaObject-Informationen |
| `pyside6-qtpy2cpp` | Konvertiert Python-Qt-Code in C++ (experimentell) |

