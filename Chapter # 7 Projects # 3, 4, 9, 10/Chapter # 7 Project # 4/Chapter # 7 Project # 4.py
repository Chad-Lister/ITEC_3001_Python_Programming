"""
Program:  recursiveRectangles.py
Author:  Chad Lister
Date:  01/03/2021

This program draws 3 rectangles using a 1/3 and 2/3 formula given in the assignment.

1)  Computation is:

        fill background with random color
        using recursion
        fill first 1/3 with random color
        fill bottom 2/3 with random color

2)  Output is:

        a canvas with 3 rectangles of random colors

"""

from turtle import Turtle
import random

# Random color list since rgb doesn't work.
color = ["black", "red", "green", "blue", "yellow", "gray", "white"]

def fillRectangle(newTurtle, height, width, x, y):
    """ Draws and fills a rectangle. """

    newTurtle.up()
    newTurtle.goto(x, y)
    newTurtle.down()
    newTurtle.begin_fill()
    newTurtle.forward(width)
    newTurtle.right(90)
    newTurtle.forward(height)
    newTurtle.right(90)
    newTurtle.forward(width)
    newTurtle.right(90)
    newTurtle.forward(height)
    newTurtle.right(90)
    newTurtle.end_fill()

    return

def main():
    """ The main function. """

    # define parameters.
    newTurtle = Turtle()
    newTurtle.speed(30)
    newTurtle.hideturtle()

    #newTurtle.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    height = newTurtle.screen.window_height()
    width = newTurtle.screen.window_width()
    x = -360
    y = 360

    # initial background..
    newTurtle.fillcolor(color[random.randint(0, 6)])
    fillRectangle(newTurtle, height, width, x, y)
    
    x = -136
    y = 360
    width = (width / 3 + 2) * 2
    c = 1

    for c in range(2):
        
        newTurtle.fillcolor(color[random.randint(0, 6)])
        fillRectangle(newTurtle, height, width, x, y)
        x = -360
        y = 136
        height = (height / 3 + 2) * 2
        width = newTurtle.screen.window_width()

    return

main()
