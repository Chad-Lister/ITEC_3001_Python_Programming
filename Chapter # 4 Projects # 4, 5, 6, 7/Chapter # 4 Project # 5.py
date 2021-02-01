""""
Program:  shifleft.py
Author:  Chad Lister
Date:  12/16/2020

This program takes a bianary string and shifts it one position left, displaying the resulting string.

1.  The input is:

        bianaryString

2.  Computation is:

        tempChar = bianaryString[0]
        newChar = ""
        index = 0
        shiftedString = ""

        for index in range(len(bianaryString) - 1):

            newChar = bianaryString [index + 1]
            shiftedString += newChar
            index += 1

        shiftedString += tempChar

3.  The output is:

        the shifted string
"""

# Get input from user

bianaryString = str(input("Please enter a string of bianary numbers to shift left:  "))

# Initialize variables

tempChar = bianaryString[0]
newChar = ""
index = 0
shiftedString = ""

# Compute shift left 1

for index in range(len(bianaryString) - 1):

    newChar = bianaryString[index + 1]
    shiftedString += newChar
    index += 1

shiftedString += tempChar

#Display output

print("The shifted string is:  ", shiftedString)
