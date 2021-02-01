"""
Program:  sharpen.py
Author:  Chad Lister
Date:  01/04/2021

Define a function that keeps the original image but sharpens it's edges.

1)  Input is:

        an image with an integer to sharpen and an integer to detect the edges.

2)  Computation is:

        If it's and edge add sharpen else subtract sharpen

3)  Output is:

        The sharpened image.
        
"""

from images import Image

def sharpen(image, sharp, threshold):
    """ Sharpens the given image by the amount indicated using the threshold for edge detection. """

    new = image.clone()

    def average(triple):
        """ Gets average of r, g, b values. """
        (r, g, b) = triple
        return (r + g + b) / 3

    # for pixels in image.
    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):

            # get left, original and bottom pixel and their averages.
            originalPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(originalPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)

            if abs(oldLum - leftLum) > threshold or abs(oldLum - bottomLum) > threshold:
                (r, g, b) = image.getPixel(x, y)

                # threshold check.
                if r + sharp <= 255 and g + sharp <= 255 and b + sharp <= 255:

                    # edge detected so sharpen.
                    new.setPixel(x, y, (r + sharp, g + sharp, b + sharp))
            else:
                (r, g, b) = image.getPixel(x, y)
                if r - sharp >= 0 and g - sharp >= 0 and b - sharp >= 0:

                    # mute color.
                    new.setPixel(x, y, (r - sharp, g - sharp, b - sharp))

    return new

def main():
    """ The main function. """

    # get user input.
    file = str(input("Please enter an image name (.gif only):  "))
    image = Image(file)
    sharp = int(input("Please enter an integer to sharpen the image by:  "))
    threshold = int(input("Please enter an integer threshold for edge detection:  "))
    
    sharpen(image, sharp, threshold)
    print("Close the image window to exit.")
    image.draw()
    
    return

main()
