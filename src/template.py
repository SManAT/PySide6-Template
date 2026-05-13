import sys
from pathlib import Path

from PySide6.QtGui import QIcon, QPixmap
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
        path_to_icon = "assets/app.ico"  # relative to the project root
        pixmap = QPixmap()
        pixmap.loadFromData(Path(path_to_icon).read_bytes())
        appIcon = QIcon(pixmap)
        self.setWindowIcon(appIcon)

        # Connect events ----------------------------
        self.ui.SSID.setPlainText("Mein WLAN --------------")

        inhalt = self.ui.SSID.toPlainText()
        print(inhalt)

        # self.ui.closeBtn_2.clicked.connect(lambda: self.parameter(12))
        self.ui.closeBtn_2.clicked.connect(self.btnClick)

        # show the window
        self.show()

    def btnClick(self):
        print("Button wurde ANGEKLICKT")

    def load_stylesheet(self, file_path):
        css_path = Path.joinpath(self.rootDir, "css", file_path)
        try:
            with open(css_path, "r", encoding="utf-8") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"CSS file '{css_path}' not found")

    def closeEvent(self, event):
        """catch the closing Event"""
        print("X is clicked: I'm now closing ...")

    def window_close(self):
        """exit the app"""
        app.quit()


if __name__ == "__main__":
    jls_extract_var = QApplication
    app = jls_extract_var(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
