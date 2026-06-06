import sys
from pathlib import Path

from PySide6 import QtGui
from PySide6.QtGui import QIcon, QPixmap, QScreen
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.rootDir = Path(__file__).parent

        # Setup UI using compiled file after using UIC
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Load stylesheet after UI setup
        self.load_stylesheet("styles.css")

        # UI Stuff ---------------------------------
        self.setWindowTitle("Mein erstes Fenster")

        # load window icon
        icon_path = self.rootDir.parent / "assets" / "app.ico"
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

    def center(self):
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def createQRCode(self, filename):
        import qrcode

        data = f"WIFI:T:WPA;S:{self.ssid};P:{self.password};;"
        print(data)
        qr = qrcode.QRCode(version=1, box_size=10, border=5, error_correction=qrcode.constants.ERROR_CORRECT_M)  # pyright: ignore[reportAttributeAccessIssue]
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)

    def setQRImage(self, filename):
        """Load PNG and fit to label"""
        pixmap = QtGui.QPixmap(filename)
        # Scale to fit label size
        # scaled = pixmap.scaledToWidth(self.ui.img.width(), QtCore.Qt.SmoothTransformation)
        if pixmap.isNull() is False:
            self.ui.img.setPixmap(pixmap)

    def btnClick(self):
        print("Button wurde ANGEKLICKT")
        filename = "QRCode_SSID.png"
        self.createQRCode(filename)
        self.setQRImage(filename)

    def load_stylesheet(self, file_path):
        css_path = Path.joinpath(self.rootDir, "css", file_path)
        try:
            with open(css_path, "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS file '{css_path}' not found")

    def closeEvent(self, event) -> None:
        """catch the closing Event"""
        print("X is clicked: I'm now closing ...")

    def window_close(self) -> None:
        """exit the app"""
        app.quit()


if __name__ == "__main__":
    jls_extract_var = QApplication
    app = jls_extract_var(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
