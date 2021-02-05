"""
Program:  selection.py
Author:  Chad Lister
Date: 01/21/2021

This program is the selection sort given in the book for

DS Chpter # 3 Project # 5:

    Modify the selection sort function discussed so the user can choose
    ascending or decending order.

"""

def swap(lyst, i , j):
    
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def selectionSort(lyst):

    i = 0
    while i < len(lyst) - 1:

        minIndex = i
        j = i + 1

        while j < len(lyst):

            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1

        if minIndex != i:
            swap(lyst, minIndex, i)

        i += 1

    print("The sorted list is", lyst)


def main():
    """ The main function. """
    
    lyst = [99, 18, 24, 55, 2, 67, 4, 77, 80]
    selectionSort(lyst)

main()
