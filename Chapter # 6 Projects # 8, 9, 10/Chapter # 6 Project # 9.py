"""
Program:  sumnumbers.py
Author:  Chad Lister
Date:  12/23/2020

This program sums the numbers in a text file and their average using 2 high order functions.
High order functions used are map and reduce.

1)  Input is:

        a text file

2)  Computation is:

        for the lines in a file.
        divide into words.
        if it is a diigit then add to a list and add 1 to count.
        map the numbers in line to int.
        add int to total to get sum.
        divide sum by count to get average.
        
3)  Output is:

        the sum of the numbers in the file and their average

"""

from functools import reduce

averageTotal = 0

def main():
    """  The main function. """
    sum_of_numbers("sum.txt")

# The add funtion.
def add(x, y):
    """ Adds two numbers together. """
    return x + y

# Sum numbers in file function.
def sum_of_numbers(fileName):
    """ Sums the numbers in a text file using 2 high order functions. """

    # variables
    file = open(fileName, 'r')
    mapList = []
    listTotal = 0
    sumTotal = 0
    average = 0
    averageTotal = int(0)

    # For lines in file read, strip and divide into words
    for lines in file:

        digitList = []
        line = lines.strip()
        words = lines.split()

        # For words in line check if it is a digit
        for word in words:

            if word.isdigit() == True:

                digitList.append(word)
                average += 1

        # Map values, reduce to int and add to sum
        print("The numbers in the line are ", digitList)
        mapList = list(map(int, digitList))
        listTotal = reduce(add, mapList)

        sumTotal += listTotal
        averageTotal = int(sumTotal / average)
    
    return print("The digits in the file total:  ", sumTotal, ".  Their average is", averageTotal, ".")

main()
