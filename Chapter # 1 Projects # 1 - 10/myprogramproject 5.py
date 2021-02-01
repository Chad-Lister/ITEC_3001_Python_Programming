"""

Program:  myprogramproject 5.py
Author:  Chad Lister

Computes the area of a triangle.

1.  Significant constants:
         None.

2.  The inputs are:
        base
        height

3.  Computations:
         area = .5 * base * height

4.  The output is:
         The area of the triangle
"""

# Request the inputs
base = int(input("Enter the base:  "))
height = int(input("Enter the height:  "))

#  Compute the area
area = .5 * base * height

#  Display the area
print("The area is ", area, " .")
