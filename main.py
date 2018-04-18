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
import os

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

        #RGB sliders
        vbox2 = QVBoxLayout()
        self.sl = QSlider(Qt.Horizontal, self)
        self.sl.setMinimum(-50)
        self.sl.setMaximum(50)
        self.sl.setValue(0)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(5)
        self.s2 = QSlider(Qt.Horizontal, self)
        self.s2.setMinimum(-50)
        self.s2.setMaximum(50)
        self.s2.setValue(0)
        self.s2.setTickPosition(QSlider.TicksBelow)
        self.s2.setTickInterval(5)
        self.s3 = QSlider(Qt.Horizontal, self)
        self.s3.setMinimum(-50)
        self.s3.setMaximum(50)
        self.s3.setValue(0)
        self.s3.setTickPosition(QSlider.TicksBelow)
        self.s3.setTickInterval(5)
        vbox2.addWidget(self.s1)
        vbox2.addWidget(self.s2)
        vbox2.addWidget(self.s3)
        self.sl.valueChanged.connect(self.redValueChange)
        self.s2.valueChanged.connect(self.greenValueChange)
        self.s3.valueChanged.connect(self.blueValueChange)

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
    @pyqtSlot
    def redValueChange(self):
        value = self.sl.value()
        im = Image.open(self.picToEdit)
    @pyqtSlot
    def greenValueChange(self):
        value = self.s2.value()
        im = Image.open(self.picToEdit)
    @pyqtSlot
    def blueValueChange(self):
        value = self.s3.value()
        im = Image.open(self.picToEdit)
    #PUT THIS WHEN WRITING NEW FUNCTIONS
    #*******************************************************************************************************
    # Function
    # Summary:
    #*******************************************************************************************************


app = QApplication(sys.argv)
page = MainPage()
status = app.exec_()
sys.exit(status)
