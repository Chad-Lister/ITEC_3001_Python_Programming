"""
Program:  areaofcircle.py
Author:  Chad Lister

Computes the area of a circle.

1.  Significant constants:
         none

2.  The input is:
         radius

3.  Computations:
         area = 3.14 * radius ** 2

4.  The output is:
         the circles area
"""

#  Request inputs
radius = float(input("Please enter the radius of the circle:  "))

#  Compute the area
area = 3.14 * radius ** 2

#  Display the area of the circle
print("The area of the circle is ", area, " .")
