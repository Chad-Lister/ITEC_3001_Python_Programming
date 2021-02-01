"""
Program:  decimalToOctal.py
Author:  Chad Lister
Date:  12/16/2020

This program converts a decimal string to an octal number.

1.  The inout is:

        decimalString

2.  Computations:

        if decimal == 0: 
            print(0)
        else:
            bstring = ""
            while decimal > 0:
                remainder = decimal % 8
                decimal = decimal // 8
                bstring = str(remainder) + bstring

3.  The output is:

        the octal value of the string

"""

# Get input from user

decimal = int(input("Enter a decimal integer:  "))

# Initialize variables

octalString = ""

# Compute decimal integer

if decimal == 0: 
    print(0)
else:
    
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        octalString = str(remainder) + octalString

# Display value

print("The octal representation is", octalString)
