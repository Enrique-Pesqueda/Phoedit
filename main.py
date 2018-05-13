#*******************************************************************************************************
# main.py
# Contributors: Enrique Mosqueda, Samuel Peters, Tristan Martin, Sebastian Ruiz
# Last Changed: 14 April 2018
# Description: This is the main file that brings all of the pyqt layouts together to create the completed GUI.
#*******************************************************************************************************
import sys
import pickle
from FileDialog import FileDialog
import histogramFunctions
from ImageManipFunctions import ImageManipFunctions
from PyQt5.QtWidgets import *
from FilterFunctions import Filters
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
        self.imageHeight = 0
        self.imageWidth = 0

        #FILE EXPLORER / IMAGE DISPLAY / HISTOGRAM LAYOUT
        self.displayPicText = QLabel('File Location: ' + self.originalPic)
        self.displayPicHolder = QLabel(self)
        self.displayPic = QPixmap(self.originalPic)
        self.displayPic = self.displayPic.scaled(300, 300, Qt.KeepAspectRatio)
        self.displayPicHolder.setPixmap(self.displayPic)
        self.fileExplorerButton = QPushButton('Choose Image to Edit')
            #main upper box
            #creates new Histograms
        histogramFunctions.run(self.destination)
        self.topBox = QHBoxLayout()
        self.leftTopBox = QVBoxLayout()
            #left box inside of topBox
        self.leftTopBox.addWidget(self.fileExplorerButton)
        self.leftTopBox.addWidget(self.displayPicText)
        self.leftTopBox.addWidget(self.displayPicHolder)
            #rght box inside topBox
        self.rightTopBox = QVBoxLayout()
        self.histogramText = QLabel('Histograms')
        self.histogramText.setFont(QFont('SansSerif', 15))
        self.rightTopBox.addWidget(self.histogramText)
            #red
        self.redHistogramHolder = QLabel()
        self.redHistogram = QPixmap('images/red.png')
        self.redHistogram = self.redHistogram.scaled(150, 150, Qt.KeepAspectRatio)
        self.redHistogramHolder.setPixmap(self.redHistogram)
                #green
        self.greenHistogramHolder = QLabel()
        self.greenHistogram = QPixmap('images/green.png')
        self.greenHistogram = self.greenHistogram.scaled(150, 150, Qt.KeepAspectRatio)
        self.greenHistogramHolder.setPixmap(self.greenHistogram)
                #blue
        self.blueHistogramHolder = QLabel()
        self.blueHistogram = QPixmap('images/blue.png')
        self.blueHistogram = self.blueHistogram.scaled(150, 150, Qt.KeepAspectRatio)
        self.blueHistogramHolder.setPixmap(self.blueHistogram)
                #add red greed blue
        self.topBoxRightTopBox = QHBoxLayout()
        self.topBoxRightTopBox.addWidget(self.redHistogramHolder)
        self.topBoxRightTopBox.addWidget(self.greenHistogramHolder)
        self.bottomBoxRightTopBox = QHBoxLayout()
        self.bottomBoxRightTopBox.addWidget(self.blueHistogramHolder)
        self.rightTopBox.addLayout(self.topBoxRightTopBox)
        self.rightTopBox.addLayout(self.bottomBoxRightTopBox)
        self.topBox.addLayout(self.leftTopBox)
        self.topBox.addLayout(self.rightTopBox)

        #IMAGE MANIPULATION SLIDERS LAYOUT
            #saturation sliders
        self.rightBottomBox = QVBoxLayout()
        self.leftBottomBox = QVBoxLayout()
        self.bottomBox = QHBoxLayout()
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
        self.rightBottomBox.addLayout(self.sliderbox)
        self.bottomBox.addLayout(self.leftBottomBox)
        self.bottomBox.addLayout(self.rightBottomBox)

        #BUTTON FOR REVERT
        self.revertButton = QPushButton("Revert")
        self.leftBottomBox.addWidget(self.revertButton)

        #FILTER DROP BOX LAYOUT
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItem("Choose a Filter")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Sepia")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Gray")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Negative")
        self.leftBottomBox.addWidget(self.my_combo_box)

        #SAVE BUTTON
        self.saveButton = QPushButton("Save")
        self.leftBottomBox.addWidget(self.saveButton)

        #MAIN LAYOUT
        self.mbox = QVBoxLayout()
        self.mbox.addLayout(self.topBox)
        self.mbox.addLayout(self.bottomBox)
        self.setLayout(self.mbox)

        #FUNCTION SLOTS
        self.fileExplorerButton.clicked.connect(self.openFileExplorerWindow)
        self.s1.valueChanged.connect(self.redSaturationChange)
        self.s2.valueChanged.connect(self.greenSaturationChange)
        self.s3.valueChanged.connect(self.blueSaturationChange)
        self.s4.valueChanged.connect(self.redVibranceChange)
        self.s5.valueChanged.connect(self.greenVibranceChange)
        self.s6.valueChanged.connect(self.blueVibranceChange)
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
        self.imageHeight, self.imageWidth = im.size
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
    # Summary: This function opens the file explorer to select a location to save your current image.
    @pyqtSlot()
    def openSaveFileWindow(self):
        saveLocation = FileDialog.saveFileDialog(self)
        if saveLocation != False:
            saveLocation += FileDialog.fileExtensionGrabber(self.originalPic)
            newImage = Image.new('RGB', (self.imageHeight, self.imageWidth))
            newImage.putdata(self.picToEditData)
            newImage.save(saveLocation)
    #*******************************************************************************************************
    # Summary: This function updates the main display by deleting widgets adding new widgets with updated
    #          information to the mainpage.
    def updateMainPage(self):

        #DELETES EVERYTHING IN GUI
            #file explore / image display layout
        self.leftTopBox.removeWidget(self.displayPicText)
        self.displayPicText.deleteLater()
        self.leftTopBox.removeWidget(self.displayPicHolder)
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
        self.topBox.removeWidget(self.my_combo_box)
        self.my_combo_box.deleteLater()
            #revertButton
        self.topBox.removeWidget(self.revertButton)
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

            #delete save button
        self.leftBottomBox.removeWidget(self.saveButton)
        self.saveButton.deleteLater()

            #deletes Histograms
        self.topBoxRightTopBox.removeWidget(self.redHistogramHolder)
        self.redHistogramHolder.deleteLater()
        self.topBoxRightTopBox.removeWidget(self.greenHistogramHolder)
        self.greenHistogramHolder.deleteLater()
        self.bottomBoxRightTopBox.removeWidget(self.blueHistogramHolder)
        self.blueHistogramHolder.deleteLater()


        #CREATES NEW GUI
            #creates new Histograms
        histogramFunctions.run(self.destination)

            #adds picture diplay and picture path text
        self.displayPicText = QLabel('File Location: ' + self.originalPic)
        self.displayPicHolder = QLabel(self)
        self.displayPic = QPixmap(self.destination)
        self.displayPic = self.displayPic.scaled(300, 300, Qt.KeepAspectRatio)
        self.displayPicHolder.setPixmap(self.displayPic)
        self.leftTopBox.addWidget(self.displayPicText)
        self.leftTopBox.addWidget(self.displayPicHolder)
        # self.topBox.addLayout(self.leftTopBox)
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
        self.s456Type.setFont(QFont('SansSerif', 15))
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
        self.leftBottomBox.addWidget(self.revertButton)
        self.revertButton.clicked.connect(self.revertToOrigin)
            # Adds Dropbox
        self.my_combo_box = QComboBox()
        self.my_combo_box.addItem("Choose a Filter")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Sepia")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Gray")
        self.my_combo_box.addItem(QIcon(self.originalPic), "Negative")
        self.leftBottomBox.addWidget(self.my_combo_box)

        #adds save button
        self.saveButton = QPushButton("Save")
        self.leftBottomBox.addWidget(self.saveButton)

        if self.originalPic != 'images/noImageSelected.jpg' and self.destination != 'images/noImageSelected.jpg':
            self.my_combo_box.currentIndexChanged.connect(self.selectionChange)
            self.saveButton.clicked.connect(self.openSaveFileWindow)
            #rght box inside topBox
            #red
        self.redHistogramHolder = QLabel()
        self.redHistogram = QPixmap('images/red.png')
        self.redHistogram = self.redHistogram.scaled(150, 150, Qt.KeepAspectRatio)
        self.redHistogramHolder.setPixmap(self.redHistogram)
                #green
        self.greenHistogramHolder = QLabel()
        self.greenHistogram = QPixmap('images/green.png')
        self.greenHistogram = self.greenHistogram.scaled(150, 150, Qt.KeepAspectRatio)
        self.greenHistogramHolder.setPixmap(self.greenHistogram)
                #blue
        self.blueHistogramHolder = QLabel()
        self.blueHistogram = QPixmap('images/blue.png')
        self.blueHistogram = self.blueHistogram.scaled(150, 150, Qt.KeepAspectRatio)
        self.blueHistogramHolder.setPixmap(self.blueHistogram)
                #add red greed blue
        self.topBoxRightTopBox.addWidget(self.redHistogramHolder)
        self.topBoxRightTopBox.addWidget(self.greenHistogramHolder)
        self.bottomBoxRightTopBox.addWidget(self.blueHistogramHolder)

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
        value = self.s4.value()
        temp = value
        value = ImageManipFunctions.valueArithmeticAdvancedRecordKeepingFunction(value, self.redVibranceValue)
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
