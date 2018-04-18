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
    # Summary: This function initializes the Main window which will contain the image being edited and all
    #          possible editing options for that image.
    def __init__(self):
        super().__init__()
        #WINDOW SETTINGS
        self.setWindowTitle("phoEDIT")
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)

        #IMPORTANT VARIABLES
        self.picToEdit=''
        self.OriginalPic = 'noImageSelected.jpg'



        #FILE EXPLORER / IMAGE DISPLAY LAYOUT
        self.displayPicText = QLabel(self.picToEdit)
        self.displayPicHolder = QLabel(self)
        self.displayPic = QPixmap(self.picToEdit)
        self.displayPic = self.displayPic.scaled(300, 300, Qt.KeepAspectRatio)
        self.displayPicHolder.setPixmap(self.displayPic)
        self.fileExplorerButton = QPushButton('Choose Image to Edit')
        self.vbox1 = QVBoxLayout()
        self.vbox1.addWidget(self.fileExplorerButton)
        self.vbox1.addWidget(self.displayPicText)
        self.vbox1.addWidget(self.displayPicHolder)

        #MAIN LAYOUT
        self.mbox = QVBoxLayout()
        self.mbox.addLayout(self.vbox1)
        self.setLayout(self.mbox)
        self.setGeometry(0, 0, 800, 600)

        #FUNCTION SLOTS
        self.fileExplorerButton.clicked.connect(self.openFileExplorerWindow)

        #SHOW EVERYTHING
        self.show()
    #*******************************************************************************************************
    # Summary: This function opens the file explorer to select an image to be edited. This changes the
    #          current photo being displayed and the file path text that is displayed to the corresponding image
    #          file.
    @pyqtSlot()
    def openFileExplorerWindow(self):
        self.picToEdit = FileExplorer.openFileNameDialog(self)
        self.updateMainPage()
    #*******************************************************************************************************
    # Summary: This function updates the main display by deleting widgets adding new widgets with updated
    #          information to the mainpage.
    def updateMainPage(self):
        #updates picture display and file path text display
        self.vbox1.removeWidget(self.displayPicText)
        self.displayPicText.deleteLater()
        self.vbox1.removeWidget(self.displayPicHolder)
        self.displayPicHolder.deleteLater()
        self.displayPicText = QLabel(self.picToEdit)
        self.displayPicHolder = QLabel(self)
        self.displayPic = QPixmap(self.picToEdit)
        self.displayPic = self.displayPic.scaled(300, 300, Qt.KeepAspectRatio)
        self.displayPicHolder.setPixmap(self.displayPic)
        self.vbox1.addWidget(self.displayPicText)
        self.vbox1.addWidget(self.displayPicHolder)
    #*******************************************************************************************************


    #PUT THIS WHEN WRITING NEW FUNCTIONS
    #*******************************************************************************************************
    # Summary:
    # Function
    #*******************************************************************************************************

app = QApplication(sys.argv)
page = MainPage()
status = app.exec_()
sys.exit(status)
