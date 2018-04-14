
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QLabel
from PIL import Image
from PyQt5.QtGui import QIcon, QPixmap

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PhoeEdit")

        #MAIN LAYOUT
        mbox = QVBoxLayout()
        self.setLayout(mbox)

        #SHOW EVERYTHING
        self.show()

app = QApplication(sys.argv)
page = MainPage()
status = app.exec_()
sys.exit(status)
