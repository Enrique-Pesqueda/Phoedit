#*******************************************************************************************************
# FileExplorer.py
# Contributors: Samuel Peters
# Last Changed: 14 April 2018
# Description: This
#*******************************************************************************************************
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FileExplorer(QWidget):

    #*******************************************************************************************************
    # Summary: This function displays a file explorer window that can be used to choose an image file to edit.
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Photo to Edit", "","JPG Files (*.jpg);;PNG Files (*.png)", options=options)
        if fileName:
            return fileName
    #*******************************************************************************************************
