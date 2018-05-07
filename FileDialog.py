#*******************************************************************************************************
# FileDialog.py
# Contributors: Samuel Peters
# Last Changed: 14 April 2018
# Description: This
#*******************************************************************************************************
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FileDialog(QWidget):

    #*******************************************************************************************************
    # Summary: This function displays a file explorer window that can be used to choose an image file to edit.
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Photo to Edit", "","JPG Files (*.jpg);;PNG Files (*.png)", options=options)
        if fileName:
            return fileName
        else:
            return False
    #*******************************************************************************************************
    # Summary: This function find the file extension of an image fileself.
    def fileExtensionGrabber(originalPic):
        spot = 0
        for x in range((len(originalPic) - 1), 0, -1):
            if originalPic[x] == '.':
                spot = x
                break
        return originalPic[spot:]
    #*******************************************************************************************************
