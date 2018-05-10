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
from filterFunctions import Filters
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
        self.redVibranceValue = 0
        self.greenVibranceValue = 0
        self.blueVibranceValue = 0

        #FILE EXPLORER / IMAGE DISPLAY / HISTOGRAM LAYOUT
        self.displayPicText = QLabel('File Location: ' + self.originalPic)
        self.displayPicHolder = QLabel(self)
        self.displayPic = QPixmap(self.originalPic)
        self.displayPic = self.displayPic.scaled(400, 400, Qt.KeepAspectRatio)
        self.displayPicHolder.setPixmap(self.displayPic)
        self.fileExplorerButton = QPushButton('Choose Image to Edit')
            #main upper box
        self.vbox1 = QHBoxLayout()
        self.leftUpperBox = QVBoxLayout()
            #left box inside of vbox1
        self.leftUpperBox.addWidget(self.fileExplorerButton)
        self.leftUpperBox.addWidget(self.displayPicText)
        self.leftUpperBox.addWidget(self.displayPicHolder)
            #rght box inside vbox1
        self.rightUpperBox = QHBoxLayout()
        self.redHistogramHolder = QLabel()
        self.redHistogram = QPixmap()
        self.greenHistogramHolder = QLabel()
        self.greenHistogram = QPixmap()
        self.blueHistogramHolder = QLabel()
        self.blueHistogram = QPixmap()
        self.rightUpperBox.addWidget(self.redHistogramHolder)
        self.rightUpperBox.addWidget(self.greenHistogramHolder)
        self.rightUpperBox.addWidget(self.blueHistogramHolder)
        self.vbox1.addLayout(self.leftUpperBox)
        self.vbox1.addLayout(self.rightUpperBox)

        #IMAGE MANIPULATION SLIDERS LAYOUT
            #saturation sliders
        self.vbox2 = QHBoxLayout()
        self.sliderbox = QVBoxLayout()
        self.saturationBox = QVBoxLayout()
        self.s1 = QSlider(Qt.Horizontal, self)
        self.s1.setMinimum(-50)
        self.s1.setMaximum(50)
        self.s1.setValue(0)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.setTickInterval(5)
        self.s1Text = QLabel('Red')
        self.s2 = QSlider(Qt.Horizontal, self)
        self.s2.setMinimum(-50)
        self.s2.setMaximum(50)
        self.s2.setValue(0)
        self.s2.setTickPosition(QSlider.TicksBelow)
        self.s2.setTickInterval(5)
        self.s2Text = QLabel('Green')
        self.s3 = QSlider(Qt.Horizontal, self)
        self.s3.setMinimum(-50)
        self.s3.setMaximum(50)
        self.s3.setValue(0)
        self.s3.setTickPosition(QSlider.TicksBelow)
        self.s3.setTickInterval(5)
        self.s3Text = QLabel('Blue')
        self.s123Type = QLabel('Saturation')
        self.s123Type.setFont(QFont('SansSerif', 15))
        self.saturationBox.addWidget(self.s123Type)
        self.saturationBox.addWidget(self.s1Text)
        self.saturationBox.addWidget(self.s1)
        self.saturationBox.addWidget(self.s2Text)
        self.saturationBox.addWidget(self.s2)
        self.saturationBox.addWidget(self.s3Text)
        self.saturationBox.addWidget(self.s3)
            #vibrance sliders
        self.vibranceBox = QVBoxLayout()
        self.s4 = QSlider(Qt.Horizontal, self)
        self.s4.setMinimum(0)
        self.s4.setMaximum(50)
        self.s4.setValue(0)
        self.s4.setTickPosition(QSlider.TicksBelow)
        self.s4.setTickInterval(5)
        self.s4Text = QLabel('Red')
        self.s5 = QSlider(Qt.Horizontal, self)
        self.s5.setMinimum(0)
        self.s5.setMaximum(50)
        self.s5.setValue(0)
        self.s5.setTickPosition(QSlider.TicksBelow)
        self.s5.setTickInterval(5)
        self.s5Text = QLabel('Green')
        self.s6 = QSlider(Qt.Horizontal, self)
        self.s6.setMinimum(0)
        self.s6.setMaximum(50)
        self.s6.setValue(0)
        self.s6.setTickPosition(QSlider.TicksBelow)
        self.s6.setTickInterval(5)
        self.s6Text = QLabel('Blue')
        self.s456Type = QLabel('Vibrance')
        self.s456Type.setFont(QFont('SansSerif', 15))
        self.vibranceBox.addWidget(self.s456Type)
        self.vibranceBox.addWidget(self.s4Text)
        self.vibranceBox.addWidget(self.s4)
        self.vibranceBox.addWidget(self.s5Text)
        self.vibranceBox.addWidget(self.s5)
        self.vibranceBox.addWidget(self.s6Text)
        self.vibranceBox.addWidget(self.s6)
        self.sliderbox.addLayout(self.saturationBox)
        self.sliderbox.addLayout(self.vibranceBox)
        self.vbox2.addLayout(self.sliderbox)

        #BUTTON FOR REVERT
        self.revertButton = QPushButton("Revert")
        self.vbox1.addWidget(self.revertButton)

        #FILTER DROP BOX LAYOUT
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItem("Choose a Filter")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Sepia")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Gray")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Negative")
        self.vbox1.addWidget(self.my_combo_box)

        #MAIN LAYOUT
        self.mbox = QVBoxLayout()
        self.mbox.addLayout(self.vbox1)
        self.mbox.addLayout(self.vbox2)
        self.setLayout(self.mbox)

        #FUNCTION SLOTS
        self.fileExplorerButton.clicked.connect(self.openFileExplorerWindow)
        self.s1.valueChanged.connect(self.redSaturationChange)
        self.s2.valueChanged.connect(self.greenSaturationChange)
        self.s3.valueChanged.connect(self.blueSaturationChange)
        self.s4.valueChanged.connect(self.redVibranceChange)
        self.s5.valueChanged.connect(self.greenVibranceChange)
        self.s6.valueChanged.connect(self.blueVibranceChange)
        self.my_combo_box.currentIndexChanged.connect(self.selectionChange)
        self.revertButton.clicked.connect(self.revertToOrigin)


        #SHOW EVERYTHING
        self.show()
    #*******************************************************************************************************
    # Summary: This function opens the file explorer to select an image to be edited. This changes the
    #          current photo being displayed and the file path text that is displayed to the corresponding image
    #          file.
    @pyqtSlot()
    def openFileExplorerWindow(self):
        ogPicHolder = self.originalPic
        self.originalPic = FileDialog.openFileNameDialog(self)
        if self.originalPic == False:
            self.originalPic = ogPicHolder
        self.destination = 'images/001' + FileDialog.fileExtensionGrabber(self.originalPic)
        im = Image.open(self.originalPic)
        im.save(self.destination)
        self.picToEditData = im.getdata()
        self.redSaturationValue = 0
        self.greenSaturationValue = 0
        self.blueSaturationValue = 0
        self.redVibranceValue = 0
        self.greenVibranceValue = 0
        self.blueVibranceValue = 0
        self.updateMainPage()
    #*******************************************************************************************************
    # Summary: This function updates the main display by deleting widgets adding new widgets with updated
    #          information to the mainpage.
    def updateMainPage(self):

        #DELETES EVERYTHING IN GUI
            #file explore / image display layout
        self.leftUpperBox.removeWidget(self.displayPicText)
        self.displayPicText.deleteLater()
        self.leftUpperBox.removeWidget(self.displayPicHolder)
        self.displayPicHolder.deleteLater()
            #image manipulation sliders layout
        self.saturationBox.removeWidget(self.s1)
        self.s1.deleteLater()
        self.saturationBox.removeWidget(self.s2)
        self.s2.deleteLater()
        self.saturationBox.removeWidget(self.s3)
        self.s3.deleteLater()
        self.vibranceBox.removeWidget(self.s4)
        self.s4.deleteLater()
        self.vibranceBox.removeWidget(self.s5)
        self.s5.deleteLater()
        self.vibranceBox.removeWidget(self.s6)
        self.s6.deleteLater()
            #filter dropbox layout
        self.vbox1.removeWidget(self.my_combo_box)
        self.my_combo_box.deleteLater()
            #revertButton
        self.vbox1.removeWidget(self.revertButton)
        self.revertButton.deleteLater()

        self.vibranceBox.removeWidget(self.s123Type)
        self.s123Type.deleteLater()
        self.vibranceBox.removeWidget(self.s1Text)
        self.s1Text.deleteLater()
        self.vibranceBox.removeWidget(self.s2Text)
        self.s2Text.deleteLater()
        self.vibranceBox.removeWidget(self.s3Text)
        self.s3Text.deleteLater()
        self.vibranceBox.removeWidget(self.s456Type)
        self.s456Type.deleteLater()
        self.vibranceBox.removeWidget(self.s4Text)
        self.s4Text.deleteLater()
        self.vibranceBox.removeWidget(self.s5Text)
        self.s5Text.deleteLater()
        self.vibranceBox.removeWidget(self.s6Text)
        self.s6Text.deleteLater()

        #CREATES NEW GUI
            #adds picture diplay and picture path text
        self.displayPicText = QLabel('File Location: ' + self.originalPic)
        self.displayPicHolder = QLabel(self)
        self.displayPic = QPixmap(self.destination)
        self.displayPic = self.displayPic.scaled(400, 400, Qt.KeepAspectRatio)
        self.displayPicHolder.setPixmap(self.displayPic)
        self.leftUpperBox.addWidget(self.displayPicText)
        self.leftUpperBox.addWidget(self.displayPicHolder)
        # self.vbox1.addLayout(self.leftUpperBox)
            #adds new rgb sliders
                #saturation sliders
        self.s1 = QSlider(Qt.Horizontal, self)
        self.redLabel1 = QLabel(self.s1)
        self.s1Text = QLabel('Red')
        self.s1.setMinimum(-50)
        self.s1.setMaximum(50)
        self.s1.setValue(self.redSaturationValue)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.setTickInterval(5)
        self.s2 = QSlider(Qt.Horizontal, self)
        self.greenLabel1 = QLabel(self.s2)
        self.s2Text = QLabel('Green')
        self.s2.setMinimum(-50)
        self.s2.setMaximum(50)
        self.s2.setValue(self.greenSaturationValue)
        self.s2.setTickPosition(QSlider.TicksBelow)
        self.s2.setTickInterval(5)
        self.s3 = QSlider(Qt.Horizontal, self)
        self.blueLabel1 = QLabel(self.s3)
        self.s3Text = QLabel('Blue')
        self.s3.setMinimum(-50)
        self.s3.setMaximum(50)
        self.s3.setValue(self.blueSaturationValue)
        self.s3.setTickPosition(QSlider.TicksBelow)
        self.s3.setTickInterval(5)
        self.s123Type = QLabel('Saturation')
        self.s123Type.setFont(QFont('SansSerif', 15))
        self.saturationBox.addWidget(self.s123Type)
        self.saturationBox.addWidget(self.s1Text)
        self.saturationBox.addWidget(self.s1)
        self.saturationBox.addWidget(self.s2Text)
        self.saturationBox.addWidget(self.s2)
        self.saturationBox.addWidget(self.s3Text)
        self.saturationBox .addWidget(self.s3)
        self.s1.valueChanged.connect(self.redSaturationChange)
        self.s2.valueChanged.connect(self.greenSaturationChange)
        self.s3.valueChanged.connect(self.blueSaturationChange)
                #vibrance sliders
        self.s4 = QSlider(Qt.Horizontal, self)
        self.redLabel2 = QLabel(self.s4)
        self.s4Text = QLabel('Red')
        self.s4.setMinimum(0)
        self.s4.setMaximum(50)
        self.s4.setValue(self.redVibranceValue)
        self.s4.setTickPosition(QSlider.TicksBelow)
        self.s4.setTickInterval(5)
        self.s5 = QSlider(Qt.Horizontal, self)
        self.greenLabel2 = QLabel(self.s5)
        self.s5Text = QLabel('Green')
        self.s5.setMinimum(0)
        self.s5.setMaximum(50)
        self.s5.setValue(self.greenVibranceValue)
        self.s5.setTickPosition(QSlider.TicksBelow)
        self.s5.setTickInterval(5)
        self.s6 = QSlider(Qt.Horizontal, self)
        self.blueLabel2 = QLabel(self.s6)
        self.s6Text = QLabel('Blue')
        self.s6.setMinimum(0)
        self.s6.setMaximum(50)
        self.s6.setValue(self.blueVibranceValue)
        self.s6.setTickPosition(QSlider.TicksBelow)
        self.s6.setTickInterval(5)
        self.s456Type = QLabel('Vibrance')
        self.vibranceBox.addWidget(self.s456Type)
        self.vibranceBox.addWidget(self.s4Text)
        self.vibranceBox.addWidget(self.s4)
        self.vibranceBox.addWidget(self.s5Text)
        self.vibranceBox.addWidget(self.s5)
        self.vibranceBox.addWidget(self.s6Text)
        self.vibranceBox.addWidget(self.s6)
        self.s4.valueChanged.connect(self.redVibranceChange)
        self.s5.valueChanged.connect(self.greenVibranceChange)
        self.s6.valueChanged.connect(self.blueVibranceChange)
            # Adds revert button
        self.revertButton = QPushButton("Revert")
        self.vbox1.addWidget(self.revertButton)
        self.revertButton.clicked.connect(self.revertToOrigin)
            # Adds Dropbox
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItem("Choose a Filter")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Sepia")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Gray")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Negative")
        self.vbox1.addWidget(self.my_combo_box)
        self.my_combo_box.currentIndexChanged.connect(self.selectionChange)

    #*******************************************************************************************************
    # Summary: Links to RGB saturation sliders and calls image manipulation functions  from
    #          ImageManipFunctions class.
    @pyqtSlot()
    def redSaturationChange(self):
        value = self.s1.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.redSaturationValue)
        self.picToEditData = ImageManipFunctions.redSaturation(self.picToEditData, value, self.destination)
        self.redSaturationValue = temp
        self.updateMainPage()

    @pyqtSlot()
    def greenSaturationChange(self):
        value = self.s2.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.greenSaturationValue)
        self.picToEditData = ImageManipFunctions.greenSaturation(self.picToEditData, value, self.destination)
        self.greenSaturationValue = temp
        self.updateMainPage()

    @pyqtSlot()
    def blueSaturationChange(self):
        value = self.s3.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.blueSaturationValue)
        self.picToEditData = ImageManipFunctions.blueSaturation(self.picToEditData, value, self.destination)
        self.blueSaturationValue = temp
        self.updateMainPage()

    @pyqtSlot()
    def redVibranceChange(self):
        print(self.redSaturationValue)
        value = self.s4.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.redVibranceValue)
        print(value)
        self.picToEditData = ImageManipFunctions.redVibrance(self.picToEditData, value, self.destination)
        self.redVibranceValue = temp
        self.updateMainPage()

    @pyqtSlot()
    def greenVibranceChange(self):
        value = self.s5.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.greenVibranceValue)
        self.picToEditData = ImageManipFunctions.greenVibrance(self.picToEditData, value, self.destination)
        self.greenVibranceValue = temp
        self.updateMainPage()

    @pyqtSlot()
    def blueVibranceChange(self):
        value = self.s6.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.greenVibranceValue)
        self.picToEditData = ImageManipFunctions.blueVibrance(self.picToEditData, value, self.destination)
        self.blueVibranceValue = temp
        self.updateMainPage()

    #*******************************************************************************************************
    #Summary: Connects dropdown box to fucnctions that will apply filters
    def selectionChange(self, i):
        if(i is 1):
            self.applySepiaFilter()
        if(i is 2):
            self.applyGrayFilter()
        if(i is 3):
            self.applyNegativeFilter()
    #*******************************************************************************************************
    # Summary: These function will apply filter to the picToEditData
    @pyqtSlot()
    def applySepiaFilter(self):
        print("Sepia Filter Applied")
        im = Image.open(self.originalPic)
        self.picToEditData = im.getdata()
        self.picToEditData = Filters.Sepia(self.picToEditData, self.destination)
        self.redSaturationValue = 0
        self.greenSaturationValue = 0
        self.blueSaturationValue = 0
        self.redVibranceValue = 0
        self.greenVibranceValue = 0
        self.blueVibranceValue = 0
        self.updateMainPage()
    @pyqtSlot()
    def applyGrayFilter(self):
        print("Gray Filter Applied")
        im = Image.open(self.originalPic)
        self.picToEditData = im.getdata()
        self.picToEditData = Filters.Gray(self.picToEditData, self.destination)
        self.redSaturationValue = 0
        self.greenSaturationValue = 0
        self.blueSaturationValue = 0
        self.redVibranceValue = 0
        self.greenVibranceValue = 0
        self.blueVibranceValue = 0
        self.updateMainPage()
    @pyqtSlot()
    def applyNegativeFilter(self):
        print("Negative Filter Applied")
        im = Image.open(self.originalPic)
        self.picToEditData = im.getdata()
        self.picToEditData = Filters.Neg(self.picToEditData, self.destination)
        self.redSaturationValue = 0
        self.greenSaturationValue = 0
        self.blueSaturationValue = 0
        self.redVibranceValue = 0
        self.greenVibranceValue = 0
        self.blueVibranceValue = 0
        self.updateMainPage()
    #*******************************************************************************************************
    # Summary:
    @pyqtSlot()
    def revertToOrigin(self):
        print("Image reverted")
        im = Image.open(self.originalPic)
        self.picToEditData = im.getdata()
        im.save(self.destination)
        self.redSaturationValue = 0
        self.greenSaturationValue = 0
        self.blueSaturationValue = 0
        self.redVibranceValue = 0
        self.greenVibranceValue = 0
        self.blueVibranceValue = 0
        self.updateMainPage()


    #PUT THIS WHEN WRITING NEW FUNCTIONS
    #*******************************************************************************************************
    # Summary:
    # Function
    #*******************************************************************************************************

app = QApplication(sys.argv)
page = MainPage()
status = app.exec_()
sys.exit(status)
