"""
Program:  testfunction.py
Author:  Chad Lister
Date: 12/23/2020

This program tests the printAll function with tracing.

1)  The input is:

    a sequence

2)  The output is:

        a reducing sequence and tracing for sequence argument
        
"""

def printAll(seq):

    i = 1
    last = len(seq)

    if seq:

        print(seq[0])
        print(seq[i : last], "remaining sequence argument")
        printAll(seq[1 : ])

def main():
    printAll("123456789")
    printAll(("6", "5", "4", "3", "2", "1"))

main()
