from pathlib import Path
import sys

from PySide6.QtWidgets import QMainWindow

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
