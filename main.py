#*******************************************************************************************************
# Contributors: Enrique Mosqueda, Samuel Peters, Tristan Martin, Sebastian Ruiz
# Last Changed: 14 April 2018
# Description: This is the main file that brings all of the pyqt layouts together to create the completed GUI.
#*******************************************************************************************************
import sys
import dragAndDropImageFunctions as ddif
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QLabel, QSlider
from PIL import Image
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("phoEDIT")
        self.picToEdit='IMG_0321.png'

        #DRAG AND DROP / IMAGE DISPLAY LAYOUT
        displayPicText = QLabel(self.picToEdit)
        displayPicHolder = QLabel(self)
        displayPic = QPixmap(self.picToEdit)
        displayPic = displayPic.scaled(300, 300, Qt.KeepAspectRatio)
        displayPicHolder.setPixmap(displayPic)
        vbox1 = QVBoxLayout()
        vbox1.addWidget(displayPicText)
        vbox1.addWidget(displayPicHolder)

        #RGB sliders
        vbox2 = QVBoxLayout()
        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(-50)
        self.sl.setMaximum(50)
        self.sl.setValue(0)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(5)
        vbox2.addWidget(self.sl)
        self.sl.valueChanged.connect(self.valuechange)
    def valuechange(self):
        value = self.sl.value()

        #MAIN LAYOUT
        mbox = QVBoxLayout()
        mbox.addLayout(vbox1)
        mbox.addLayout(vbox2)
        self.setLayout(mbox)
        self.setGeometry(0, 0, 800, 600)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)


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
