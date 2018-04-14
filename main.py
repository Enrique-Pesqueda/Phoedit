#*******************************************************************************************************
# Contributors: Enrique Mosqueda, Samuel Peters, Tristan Martin, Sebastian Ruiz
# Last Changed: 14 April 2018
# Description: This is the main file that brings all of the pyqt layouts together to create the completed GUI.
#*******************************************************************************************************
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

    #PUT THIS WHEN WRITING NEW FUNCTIONS
    #*******************************************************************************************************
    # Function
    # Summary:
    # Preconditions:
    # Postconditions:
    #*******************************************************************************************************


app = QApplication(sys.argv)
page = MainPage()
status = app.exec_()
sys.exit(status)
