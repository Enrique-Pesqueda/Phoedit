#*******************************************************************************************************
# Contributors: Enrique Mosqueda, Samuel Peters, Tristan Martin, Sebastian Ruiz
# Last Changed: 14 April 2018
# Description: This is the main file that brings all of the pyqt layouts together to create the completed GUI.
#*******************************************************************************************************
import sys
from FileExplorer import FileExplorer
from PyQt5.QtWidgets import *
from PIL import Image
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainPage(QWidget):

    #*******************************************************************************************************
    def __init__(self):
        super().__init__()
        self.setWindowTitle("phoEDIT")
        self.picToEdit=''

        #FILE EXPLORER / IMAGE DISPLAY LAYOUT
        self.picToEdit = FileExplorer.openFileNameDialog(self)
        displayPicText = QLabel(self.picToEdit)
        displayPicHolder = QLabel(self)
        displayPic = QPixmap(self.picToEdit)
        displayPic = displayPic.scaled(300, 300, Qt.KeepAspectRatio)
        displayPicHolder.setPixmap(displayPic)
        vbox1 = QVBoxLayout()
        vbox1.addWidget(displayPicText)
        vbox1.addWidget(displayPicHolder)

        #MAIN LAYOUT
        mbox = QVBoxLayout()
        mbox.addLayout(vbox1)
        self.setLayout(mbox)
        self.setGeometry(0, 0, 800, 600)

        #SET WINDOW BACKGROUND COLOR
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)

        #SHOW EVERYTHING
        self.show()
    # Summary: This function initializes the Main window which will contain the image being edited and all possible editing options for that image.
    # Preconditions: N/A
    # Postconditions: The main window will be shown on the desktop.
    #*******************************************************************************************************


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
