import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from easyDirUI import Ui_MainWindow  # Replace with your actual UI file name
from EasyDirHistoryFetch import fetch_xml_data


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())