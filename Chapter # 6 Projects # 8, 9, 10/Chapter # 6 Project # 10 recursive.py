"""
Program:  myrange.py
Author:  Chad Lister
Date:  12/29/2020

This program mimick the range function without using the range function.

1)  The input is:

        the lower range
        the upper range
        a step value

2)  Computation is:

        get lowerBound, upperBound and stepValue
        check for errors
        recursive call to function
        add to list by step until upperBound reached
        print list

3)  Output is:

        a list containing this range by step
        
"""

# Get users input
lowerBound = int(input("Please enter a lower bound for the list:  "))
upperBound = int(input("Please enter an upper bound for the list:  "))
stepValue = int(input("Please enter a step value for the list:  "))

# Check that lowerBound is less and step is less
if lowerBound >= upperBound or stepValue >= upperBound:
    print("Lower bound or step value can't be higher than the upper bound.")

# Variables
rangeList = []

def addToList(upperBount, lowerBound):
    """ Adds to the list. """

    if lowerBound <= upperBound:
        rangeList.append(lowerBound)
        addToList(upperBound, lowerBound + stepValue)
    return

def main():

    addToList(upperBound, lowerBound)
    print("The list contains the numbers", rangeList)
    return

main()
