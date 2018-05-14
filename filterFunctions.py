#*******************************************************************************************************
# filterFunctions.py
# Contributors: Enrique Mosqueda
# Last Changed: 14 April 2018
# Description:
#*******************************************************************************************************
from PIL import Image


class Filters():

	def Gray(imageData, destination):
		new_list = []
		for pixel in imageData:
			pixelR = int(pixel[0] * 0.21)
			pixelG = int(pixel[1] * 0.71)
			pixelB = int(pixel[2] * 0.07)
			pixelS = int((pixelR + pixelG + pixelB)/3)
			temp = (pixelS, pixelS, pixelS)
			new_list.append(temp)
		imageData = 0
		im = Image.open(destination)
		im.putdata(new_list)
		im.save(destination)
		return new_list				

	def Neg(imageData, destination):
		new_list = []
		for pixel in imageData:
			pixelR = 255 - pixel[0]
			pixelG = 255 - pixel[1]
			pixelB = 255 - pixel[2]
			temp = (pixelR, pixelG, pixelB)
			new_list.append(temp)
		imageData = 0		
		im = Image.open(destination)
		im.putdata(new_list)
		im.save(destination)
		return new_list

	def Sepia(imageData, destination):		
		new_list = []
		for pixel in imageData:
			if(pixel[0] < 63):
				pixelR,pixelG,pixelB = int(pixel[0] * 1.1) , pixel[1] , int(pixel[2] * 0.9)
			elif(pixel[0] > 62 and pixel[0] < 92):
				pixelR,pixelG,pixelB = int(pixel[0] * 1.15), pixel[1], int(pixel[2] * 0.85)
			else:
				pixelR = int(pixel[0] * 1.08)
				if pixelR > 255:
					pixelR = 255
				pixelG, pixelB = pixel[1], int(pixel[2] * 0.5)
			temp = (pixelR, pixelG, pixelB)
			new_list.append(temp)
		imageData = 0
		im = Image.open(destination)
		im.putdata(new_list)
		im.save(destination)
		return new_list
	

