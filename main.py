#*******************************************************************************************************
# main.py
# Contributors: Enrique Mosqueda, Samuel Peters, Tristan Martin, Sebastian Ruiz
# Last Changed: 14 April 2018
# Description: This is the main file that brings all of the pyqt layouts together to create the completed GUI.
#*******************************************************************************************************
import sys
from FileDialog import FileDialog
from ImageManipFunctions import ImageManipFunctions
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
        self.picToEditData = []
        self.originalPic = 'images/noImageSelected.jpg'
        self.destination = 'images/noImageSelected.jpg'
        self.redSaturationValue = 0
        self.greenSaturationValue = 0
        self.blueSaturationValue = 0

        #FILE EXPLORER / IMAGE DISPLAY LAYOUT
        self.displayPicText = QLabel(self.originalPic)
        self.displayPicHolder = QLabel(self)
        self.displayPic = QPixmap(self.originalPic)
        self.displayPic = self.displayPic.scaled(300, 300, Qt.KeepAspectRatio)
        self.displayPicHolder.setPixmap(self.displayPic)
        self.fileExplorerButton = QPushButton('Choose Image to Edit')
        self.vbox1 = QVBoxLayout()
        self.vbox1.addWidget(self.fileExplorerButton)
        self.vbox1.addWidget(self.displayPicText)
        self.vbox1.addWidget(self.displayPicHolder)

        #IMAGE MANIPULATION SLIDERS LAYOUT
        self.vbox2 = QVBoxLayout()
        self.s1 = QSlider(Qt.Horizontal, self)
        self.s1.setMinimum(-50)
        self.s1.setMaximum(50)
        self.s1.setValue(0)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.setTickInterval(5)
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
        self.vbox2.addWidget(self.s1)
        self.vbox2.addWidget(self.s2)
        self.vbox2.addWidget(self.s3)

        #MAIN LAYOUT
        self.mbox = QVBoxLayout()
        self.mbox.addLayout(self.vbox1)
        self.mbox.addLayout(self.vbox2)
        self.setLayout(self.mbox)
        self.setGeometry(0, 0, 800, 600)

        #FUNCTION SLOTS
        self.fileExplorerButton.clicked.connect(self.openFileExplorerWindow)
        self.s1.valueChanged.connect(self.redValueChange)
        self.s2.valueChanged.connect(self.greenValueChange)
        self.s3.valueChanged.connect(self.blueValueChange)

        #SHOW EVERYTHING
        self.show()
    #*******************************************************************************************************
    # Summary: This function opens the file explorer to select an image to be edited. This changes the
    #          current photo being displayed and the file path text that is displayed to the corresponding image
    #          file.
    @pyqtSlot()
    def openFileExplorerWindow(self):
        self.originalPic = FileDialog.openFileNameDialog(self)
        self.destination = 'images/001' + FileDialog.fileExtensionGrabber(self.originalPic)
        im = Image.open(self.originalPic)
        im.save(self.destination)
        self.picToEditData = im.getdata()
        self.redSaturationValue = 0
        self.greenSaturationValue = 0
        self.blueSaturationValue = 0
        self.updateMainPage()
    #*******************************************************************************************************
    # Summary: This function updates the main display by deleting widgets adding new widgets with updated
    #          information to the mainpage.
    def updateMainPage(self):

        #DELETES EVERYTHING IN GUI
            #file explore / image display layout
        self.vbox1.removeWidget(self.displayPicText)
        self.displayPicText.deleteLater()
        self.vbox1.removeWidget(self.displayPicHolder)
        self.displayPicHolder.deleteLater()
            #image manipulation sliders layout
        self.vbox2.removeWidget(self.s1)
        self.s1.deleteLater()
        self.vbox2.removeWidget(self.s2)
        self.s2.deleteLater()
        self.vbox2.removeWidget(self.s3)
        self.s3.deleteLater()

        #CREATES NEW GUI
            #adds picture diplay and picture path text
        self.displayPicText = QLabel(self.originalPic)
        self.displayPicHolder = QLabel(self)
        self.displayPic = QPixmap(self.destination)
        self.displayPic = self.displayPic.scaled(300, 300, Qt.KeepAspectRatio)
        self.displayPicHolder.setPixmap(self.displayPic)
        self.vbox1.addWidget(self.displayPicText)
        self.vbox1.addWidget(self.displayPicHolder)
            #adds new rgb sliders
        self.s1 = QSlider(Qt.Horizontal, self)
        self.s1.setMinimum(-50)
        self.s1.setMaximum(50)
        self.s1.setValue(self.redSaturationValue)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.setTickInterval(5)
        self.s2 = QSlider(Qt.Horizontal, self)
        self.s2.setMinimum(-50)
        self.s2.setMaximum(50)
        self.s2.setValue(self.greenSaturationValue)
        self.s2.setTickPosition(QSlider.TicksBelow)
        self.s2.setTickInterval(5)
        self.s3 = QSlider(Qt.Horizontal, self)
        self.s3.setMinimum(-50)
        self.s3.setMaximum(50)
        self.s3.setValue(self.blueSaturationValue)
        self.s3.setTickPosition(QSlider.TicksBelow)
        self.s3.setTickInterval(5)
        self.vbox2.addWidget(self.s1)
        self.vbox2.addWidget(self.s2)
        self.vbox2.addWidget(self.s3)
        self.s1.valueChanged.connect(self.redValueChange)
        self.s2.valueChanged.connect(self.greenValueChange)
        self.s3.valueChanged.connect(self.blueValueChange)
    #*******************************************************************************************************
    # Summary: Links to RGB saturation sliders and calls image manipulation functions  from
    #          ImageManipFunctions class.
    @pyqtSlot()
    def redValueChange(self):
        value = self.s1.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.redSaturationValue)
        self.picToEditData = ImageManipFunctions.redSaturation(self.picToEditData, value, self.destination)
        self.redSaturationValue = temp
        self.updateMainPage()

    @pyqtSlot()
    def greenValueChange(self):
        value = self.s2.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.greenSaturationValue)
        self.picToEditData = ImageManipFunctions.greenSaturation(self.picToEditData, value, self.destination)
        self.greenSaturationValue = temp
        self.updateMainPage()

    @pyqtSlot()
    def blueValueChange(self):
        value = self.s3.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.blueSaturationValue)
        self.picToEditData = ImageManipFunctions.blueSaturation(self.picToEditData, value, self.destination)
        self.blueSaturationValue = temp
        self.updateMainPage()
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
