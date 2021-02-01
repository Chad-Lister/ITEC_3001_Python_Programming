"""
Program:  octalToDecimal.py
Author:  Chad Lister
Date:  12/16/2020

This program converts a octal string to a decimal integer.

1.  The inout is:

        octalString

2.  Computations:

        for digit in octalString:
            decimal = decimal + int(digit) * 8 ** exponent
            exponent -= 1

3.  The output is:

        the integer value of the string
        
"""

# Get input from user

octalString = input("Enter a string of octal numbers:  ")

# Initialize variables

decimal = 0
exponent = len(octalString) - 1

# Compute decimal integer

for digit in octalString:
    decimal += int(digit) * 8 ** exponent
    exponent -= 1

# Display value

print("The integer value is", decimal)
