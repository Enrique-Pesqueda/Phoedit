#*******************************************************************************************************
# Contributors: Samuel Peters
# Last Changed: 14 April 2018
# Description:
#*******************************************************************************************************
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FileExplorer(QWidget):

    #*******************************************************************************************************
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Photo to Edit", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName
            print(fileName)
    # Summary: This function displays a file explorer window that can be used to choose an image file to edit.
    # Preconditions: N/A
    # Postconditions: A string containing the full path to the chosen image file will be returned.
    #*******************************************************************************************************
