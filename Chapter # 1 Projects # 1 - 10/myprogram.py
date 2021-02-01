"""

Program:  myprogram.py
Author:  Chad Lister

Computes the area of a square or rectangle.

1.  Significant constants:
         None.

2.  The inputs are:
        width
        height
3.  Computations:
         area = width * height
4.  The output is:
         The area of the square or rectangle
"""

# Request the inputs
width = int(input("Enter the width:  "))
height = int(input("Enter the height:  "))

#  Compute the area
area = width * height

#  Display the area
print("The area is ", area, " square units.")
