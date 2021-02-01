"""
Program:  lightenDarkenColor.py
Author:  Chad Lister
Date:  01/04/2021

This program applies three image filter functions given the input.

1)  Inputs are:

        an image and value to lighten by
        an image and value to darken by
        an image and color to shift by

2)  Computations are:

        for pixels in image if adjusted value <= 255, set pixel
        for pixels in image if adjusted value >= 0, set pixel
        for pixels in image if r, g, b between 0 and 255 set pixel

3)  Outputs are:

        the filtered image
        the filtered image
        the filtered image
        
"""

from images import Image

def lighten(image, light):
    """ Lightens an image. """

    # for pixels in image; add value, check and set.
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)

            # check threshhold.
            if r + light <= 255:
                r += light
            else:
                r = 255
            if g + light <= 255:
                g += light
            else:
                g = 255
            if b + light <= 255:
                b += light
            else:
                b = 255
                
            image.setPixel(x, y, (r, g, b))

    return

def darken(image, dark):
    """ Darkens an image. """

    # for pixels in image; subtract value, check and set.
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)

            # check threshhold.
            if r - dark >= 0:
                r -= dark
            else:
                r = 0
            if g - dark >= 0:
                g -= dark
            else:
                g = 0
            if b - dark >= 0:
                b -= dark
            else:
                b = 0

            image.setPixel(x, y, (r, g, b))

    return

def colorFilter(image, color):
    """ Applies a color filter to an image. """

    # split into rgb
    rgb = []
    rgb = color.split()
    r = int(rgb[0])
    g = int(rgb[1])
    b = int(rgb[2])

    # check threshold for r, g and b
    if r >= 0 and r <= 255 and g >= 0 and g <= 255 and b >= 0 and b <= 255:

        # for pixels in image.
        for y in range(image.getHeight()):
            for x in range(image.getWidth()):
                image.setPixel(x, y, (r, g, b))

    return

def main():
    """ The main function. """

    # get input
    file = str(input("Please enter an image name (.gif only):  "))
    image = Image(file)
    print("Close window to process changes to original image.")
    image.draw()
    light = int(input("Lighten image by how much ?  "))
    lighten(image, light)
    print("Close image window to process additional changes.")
    image.draw()
    dark = int(input("Darken image by how much ?  "))
    darken(image, dark)
    print("Close image window to process additional changes.")
    image.draw()
    color = ()
    color = input("Please enter 3 int values seperated by a space:  ")
    print("Changes image to desired color.")
    colorFilter(image, color)
    print("Close image window to exit.")
    image.draw()
    
    return

main()
