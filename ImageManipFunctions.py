#*******************************************************************************************************
# imageManipFunctions.py
# Contributors: Sebastian Ruiz
# Last Changed: 25 April 2018
# Description: Saturation and Vibrance editing functions.
#*******************************************************************************************************
from PIL import Image
class ImageManipFunctions():
#*******************************************************************************************************
# Summary: Return value that will be added to color chanel after slider movement.
    def valueArithmeticAdvancedRecordKeepingFunction(value, lastRecordedValue):
        if value == lastRecordedValue:
            return 0
        elif value == 0:
            return  (-1 * lastRecordedValue)
        else:
            return (value - lastRecordedValue)
#*******************************************************************************************************
# Summary: RGB saturation functions take in a pillow image object and a value
#          the getdata() method is used to be able to alter a specific color channel
#          the specified color channel is modified by adding a passed in value to it
#          this is done for every pixel in an image and are saved into a new list
    def redSaturation(imageData, value, destination):
        new_list = []
        for pixel in imageData:
            redPixel = pixel[0] + value
            if redPixel > 255:
                redPixel = 255
            temp = (redPixel,pixel[1],pixel[2])
            new_list.append(temp)
        imageData = 0
        im = Image.open(destination)
        im.putdata(new_list)
        im.save(destination)
        return new_list

    def greenSaturation(imageData, value, destination):
        new_list = []
        for pixel in imageData:
            greenPixel = pixel[1] + value
            if greenPixel > 255:
                greenPixel = 255
            temp = (pixel[0],greenPixel,pixel[2])
            new_list.append(temp)
        imageData = 0
        im = Image.open(destination)
        im.putdata(new_list)
        im.save(destination)
        return new_list

    def blueSaturation(imageData, value, destination):
        new_list = []
        for pixel in imageData:
            bluePixel = pixel[2] + value
            if bluePixel > 255:
                bluePixel = 255
            temp = (pixel[0],pixel[1],bluePixel)
            new_list.append(temp)
        imageData = 0
        im = Image.open(destination)
        im.putdata(new_list)
        im.save(destination)
        return new_list
#*******************************************************************************************************
# Summary: RGB vibrance functions take in a pillow image object and a value
#          the getdata() method is used to be able to alter a specific color channel
#          if the specified color channel contains the largest value then that pixel is altered
    def redVibrance(imageData, value, destination):
        new_list = []
        for pixel in imageData:
            if pixel[0] > pixel[1] and pixel[0] > pixel[2]:
                redPixel = pixel[0] + (value * 2)
                if redPixel > 255:
                    redPixel = 255
                greenPixel = pixel[1] - value
                bluePixel = pixel[2] - value
                temp = (redPixel,greenPixel,bluePixel)
            else:
                temp = (pixel[0],pixel[1],pixel[2])
            new_list.append(temp)
        imageData = 0
        im = Image.open(destination)
        im.putdata(new_list)
        im.save(destination)
        return new_list

    def greenVibrance(imageData, value, destination):
        new_list = []
        for pixel in imageData:
            if pixel[1] > pixel[0] and pixel[1] > pixel[2]:
                greenPixel =  pixel[1] + (value * 2)
                if greenPixel > 255:
                    greenPixel = 255
                redPixel = pixel[0] - value
                bluePixel = pixel[2] - value
                temp = (redPixel,greenPixel,bluePixel)
            else:
                temp = (pixel[0], pixel[1], pixel[2])
            new_list.append(temp)
        imageData = 0
        im = Image.open(destination)
        im.putdata(new_list)
        im.save(destination)
        return new_list

    def blueVibrance(imageData, value, destination):
        new_list = []
        for pixel in imageData:
            if pixel[2] > pixel[1] and pixel[2] > pixel[0]:
                bluePixel = pixel[2] + (value * 2)
                if bluePixel > 255:
                    bluePixel = 255
                redPixel = pixel[0] - value
                greenPixel = pixel[1] -  value
                temp = (redPixel,greenPixel,bluePixel)
            else:
                temp = (pixel[0], pixel[1], pixel[2])
            new_list.append(temp)
        imageData = 0
        im = Image.open(destination)
        im.putdata(new_list)
        im.save(destination)
        return new_list
#*******************************************************************************************************
