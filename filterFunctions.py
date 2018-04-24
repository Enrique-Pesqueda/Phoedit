#*******************************************************************************************************
# filterFunctions.py
# Contributors: Enrique Mosqueda
# Last Changed: 14 April 2018
# Description:
#*******************************************************************************************************

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FilterPic(QWidget):

	def Gray(self, img):
		for x in range(img.width()):
			for y in range(img.height()):
				color = QColor(img.pixel(x,y)).getRgb()[:-1]
				pixelR = int(color[0]*0.21)
				pixelG = int(color[1]*0.71)
				pixelB = int(color[2]*0.07)
				pixelS = (pixelB + pixelG + pixelR)/3
				copiedValue = QtGui.qRgb(pixelS, pixelS, pixelS)
				img.setPixel(x, y, copiedValue)

	def Neg(self, img):
		for x in range(img.width()):
			for y in range(img.height()):
				color = QColor(img.pixel(x,y)).getRgb()[:-1]
				pixelR = 255 - color[0]
				pixelG = 255 - color[1]
				pixelB = 255 - color[2]
				copiedValue = QtGui.qRgb(pixelR, pixelG, pixelB)
				img.setPixel(x, y, copiedValue)

	def Sepia(self, img):
		for x in range(img.width()):
			for y in range(img.height()):
				color = QColor(img.pixel(x,y)).getRgb()[:-1]
				pixelR = int(color[0]*0.393) + int(color[0]*0.769) + int(color[0]*0.189)
				if pixelR > 255:
					pixelR = 255
				pixelG = int(color[1]*0.349) + int(color[0]*0.686) + int(color[0]*0.168)
				if pixelG > 255:
					pixelG = 255
				pixelB = int(color[2]*0.272) + int(color[0]*0.534) + int(color[0]*0.131)
				if pixelB > 255:
					pixelB = 255
				copiedValue = QtGui.qRgb(pixelR, pixelG, pixelB)
				fimg.setPixel(x, y, copiedValue)


#*******************************************************************************************************
# Summary:
# Preconditions:
# Postconditions:
#*******************************************************************************************************
