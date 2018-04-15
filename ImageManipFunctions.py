#*******************************************************************************************************
# Contributors: Sebastian Ruiz
# Last Changed: 14 April 2018
# Description: RGB saturation functions take in a pillow image object and a value
# the getdata() method is used to be able to alter a specific color channels
# the specified color channel is modified by adding a passed in value to it
# this is done for every pixel in an image and are saved into a new list
#*******************************************************************************************************
def redSaturation(image, value):
    list = image.getdata()
    new_list = []
    for pixel in image:
        pixel[0] += value
        if pixel[0] > 255:
            pixel[0] = 255
        temp = (pixel[0],pixel[1],pixel[2])
        new_list.append(temp)
    picture.putdata(new_list)
    picture.save('x')

def greenSaturation(image, value):
    list = image.getdata()
    new_list = []
    for pixel in image:
        pixel[1] += value
        if pixel[1] > 255:
            pixel[1] = 255
        temp = (pixel[0],pixel[1],pixel[2])
        new_list.append(temp)
    picture.putdata(new_list)
    picture.save('x')

def blueSaturation(image, value):
    list = image.getdata()
    new_list = []
    for pixel in image:
        pixel[2] += value
        if pixel[2] > 255:
            pixel[2] = 255
        temp = (pixel[0],pixel[1],pixel[2])
        new_list.append(temp)
    picture.putdata(new_list)
    picture.save('x')



#*******************************************************************************************************
# Summary:
# Preconditions:
# Postconditions:
#*******************************************************************************************************
