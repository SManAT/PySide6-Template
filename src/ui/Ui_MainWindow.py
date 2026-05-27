# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(591, 401)
        icon = QIcon()
        icon.addFile(u"../../assets/app.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"body{\n"
"font-size:14px;\n"
"}\n"
"\n"
"\n"
".lionBtn {\n"
"    font-size: 14px;\n"
"    background: rgba(0, 0, 0, 0.08),\n"
"                QLinearGradient(spread: pad, x1: 0, y1: 0,\n"
"                               x2: 0, y2: 1,\n"
"                               stop: 0 #e4fbff,\n"
"                               stop: 0.1 #cee6fb,\n"
"                               stop: 0.5 #a5d3fb,\n"
"                               stop: 0.51 #88c6fb,\n"
"                               stop: 1 #d5faff);\n"
"    background-clip: padding;\n"
"    border-radius: 5px;\n"
"    padding: 3px 30px 3px 30px;\n"
"    color: #242d35;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_2.addWidget(self.plainTextEdit_2, 3, 0, 1, 1)

        self.qrcode = QWidget(self.centralwidget)
        self.qrcode.setObjectName(u"qrcode")

        self.gridLayout_2.addWidget(self.qrcode, 8, 0, 1, 1)

        self.SSID = QPlainTextEdit(self.centralwidget)
        self.SSID.setObjectName(u"SSID")
        sizePolicy.setHeightForWidth(self.SSID.sizePolicy().hasHeightForWidth())
        self.SSID.setSizePolicy(sizePolicy)
        self.SSID.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        self.SSID.setFont(font)
        self.SSID.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.SSID, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy1)
        self.img.setPixmap(QPixmap(u"../../basic_qrcode.png"))
        self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.img, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 1)

        self.closeBtn_2 = QPushButton(self.centralwidget)
        self.closeBtn_2.setObjectName(u"closeBtn_2")
        self.closeBtn_2.setStyleSheet(u"background: rgba(0,0,0,0.08), \n"
"QLinearGradient( spread:pad, x1: 0, y1: 0,\n"
"                 x2: 0, y2: 1, \n"
"                 stop: 0 #e4fbff, \n"
"                 stop: 0.1 #cee6fb,\n"
"                 stop: 0.5 #a5d3fb,\n"
"                 stop: 0.51 #88c6fb,\n"
"                 stop: 1 #d5faff\n"
");\n"
"background-insets: 0 0 -1 0,0,1;\n"
"background-radius: 5,5,4;\n"
"padding: 3 30 3 30;\n"
"text-fill: #242d35;\n"
"color: #000000;\n"
"")

        self.gridLayout_2.addWidget(self.closeBtn_2, 9, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"Wirklich geheim", None))
        self.SSID.setPlainText(QCoreApplication.translate("MainWindow", u"Mein WLAN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SSID", None))
        self.img.setText("")
        self.closeBtn_2.setText(QCoreApplication.translate("MainWindow", u"QR Code", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Passwort", None))
    # retranslateUi

