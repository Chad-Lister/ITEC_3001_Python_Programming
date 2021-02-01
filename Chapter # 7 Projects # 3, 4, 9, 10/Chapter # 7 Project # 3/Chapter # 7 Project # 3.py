"""
Program:  kochFractal.py
Author:  Chad Lister
Date:  01/02/2021

This program draws the Koch snowflake at a given level.

1)  Input is:

        the level of the figure

2)  Computation is:

        for 3 sides draw one line and turn
        if level is > 0 cycle thru recursion

3)  The Output is:

        the figure drawn
"""

from turtle import Turtle

def drawFractalLine(newTurtle, newSegment, levels):
    """ Draws the Koch snowflake at a given level. """

    # Draw one line only.
    if levels == 0:
        newTurtle.forward(newSegment)
        return

    # Recursive calls for other levels.
    newSegment = newSegment // 3
    drawFractalLine(newTurtle, newSegment, levels - 1)
    newTurtle.left(60)
    drawFractalLine(newTurtle, newSegment, levels - 1)
    newTurtle.right(120)
    drawFractalLine(newTurtle, newSegment, levels - 1)
    newTurtle.left(60)
    drawFractalLine(newTurtle, newSegment, levels - 1)

    return

def main():
    """ Main function. """

    # Get input and initialize parameters and move to starting position.
    levels = int(input("Please enter a level:  "))
    newTurtle = Turtle()
    newTurtle.speed(25)
    segment = 300
    newTurtle.hideturtle()
    newTurtle.up()
    newTurtle.backward(segment // 2)
    newTurtle.left(90)
    newTurtle.forward(segment // 4)
    newTurtle.right(90)
    newTurtle.down()

    # Draw the figure.
    i = 0
    for i in range(3):
        
        drawFractalLine(newTurtle, segment, levels)
        newTurtle.right(120)

    return

main()
