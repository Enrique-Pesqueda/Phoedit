#*******************************************************************************************************
# FileDialog.py
# Contributors: Samuel Peters
# Last Changed: 14 April 2018
# Description: This is code creates file dialog windows that return strings that are in reference to
#              where the picture needs to be saved. Two of these functions (openFileNameDialog and
#              saveFileDialog) were not written by us. We found these functions at https://pythonspot.com/pyqt5-file-dialog/
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
    # Summary: This function finds the file extension of an image fileself.
    def fileExtensionGrabber(originalPic):
        spot = 0
        for x in range((len(originalPic) - 1), 0, -1):
            if originalPic[x] == '.':
                spot = x
                break
        return originalPic[spot:]
    #*******************************************************************************************************
    # Summary: This function returns the loaction to save the current file.
    def saveFileDialog(self):
            fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()")
            if fileName:
                return fileName
            else:
                return False
