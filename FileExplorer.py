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
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Photo to Edit", "","PNG Files (*.png);;JPG Files (*.jpg)", options=options)
        if fileName:
            return fileName
    #*******************************************************************************************************
