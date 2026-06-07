import os
import sys
from pathlib import Path

from PySide6 import QtGui
from PySide6.QtGui import QIcon, QScreen
from PySide6.QtWidgets import QApplication, QMainWindow

from qrcode_app.ui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.rootDir = Path(__file__).parent.parent

        # Setup UI using compiled file after using UIC
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Load stylesheet after UI setup
        self.load_stylesheet("styles.css")

        # UI Stuff ---------------------------------
        self.setWindowTitle("Mein erstes Fenster")

        # load window icon
        icon_path = self.rootDir / "assets" / "app.ico"
        if icon_path.exists():
            appIcon = QIcon(str(icon_path))
            self.setWindowIcon(appIcon)

        # center on screen
        screen = QApplication.primaryScreen()
        screen_h = screen.availableGeometry().height()
        screen_w = screen.availableGeometry().width()
        self.setGeometry(0, 0, int(screen_w * 0.5), int(screen_h * 2 / 3))
        self.center()

        # Connect events ----------------------------
        self.ssid = "Schüler"
        self.password = "kindergarten123"
        self.ui.SSID.setPlainText(self.ssid)
        self.ui.password.setPlainText(self.password)

        inhalt = self.ui.SSID.toPlainText()
        print(inhalt)

        # self.ui.closeBtn_2.clicked.connect(lambda: self.parameter(12))
        self.ui.closeBtn_2.clicked.connect(self.btnClick)

        # show the window
        self.show()

    def console(self, msg):
        self.ui.consoleOutput.appendPlainText(msg)

    def center(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def createQRCode(self, filename):
        self.console("1")

        import qrcode

        data = f"WIFI:T:WPA;S:{self.ssid};P:{self.password};;"
        print(f"QR data: {data}")
        qr = qrcode.QRCode(version=1, box_size=10, border=5, error_correction=qrcode.constants.ERROR_CORRECT_M)  # pyright: ignore[reportAttributeAccessIssue]
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        self.console(f"QR image created, saving to: {filename}")

    def setQRImage(self, filename):
        """Load PNG and fit to label"""
        self.console(f"Loading image from: {filename}")
        self.console(f"File exists: {Path(filename).exists()}")

        pixmap = QtGui.QPixmap(filename)
        if pixmap.isNull():
            self.console(f"Error: Failed to load pixmap from {filename}")
        else:
            self.ui.img.setPixmap(pixmap)
            self.console(f"Image loaded successfully, setting pixmap")

    def btnClick(self):
        print("Button wurde ANGEKLICKT")
        print(f"Current working directory: {os.getcwd()}")
        print(f"sys.executable: {sys.executable}")
        print(f"__file__: {__file__}")

        output_path = Path.joinpath(self.rootDir.parent, "QRCode_SSID.png")
        print(f"Saving QR code to: {output_path}")
        try:
            self.createQRCode(str(output_path))
            print(f"QR code saved successfully")
            self.setQRImage(str(output_path))
        except Exception as e:
            print(f"Error creating/loading QR code: {e}")
            import traceback

            traceback.print_exc()

    def load_stylesheet(self, file_path):
        css_path = Path.joinpath(self.rootDir, "src", "css", file_path)
        try:
            with open(css_path, "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS file '{css_path}' not found")

    def closeEvent(self, event) -> None:
        """catch the closing Event"""
        print("X is clicked: I'm now closing ...")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
