"""
Program:  modifiedSelection.py
Author:  Chad Lister
Date: 01/21/2021

DS Chpter # 3 Project # 5:

    Modify the selection sort function discussed so the user can choose
    ascending or decending order.

"""

def swap(lyst, i , j):
    
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def selectionSort(lyst, argument):

    if argument == "up":

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

        print("\nThe sorted list is", lyst)

    elif argument == "down":

        i = 0
        while i < len(lyst) - 1:

            minIndex = i
            j = i + 1

            while j < len(lyst):

                if lyst[j] > lyst[minIndex]:
                    minIndex = j
                j += 1

            if minIndex != i:
                swap(lyst, minIndex, i)

            i += 1

        print("\nThe sorted list is", lyst)
    else:

        
        print("INVALID ORDER PASSED!")


def main():
    """ The main function. """
    
    lyst = [99, 18, 24, 55, 2, 67, 4, 77, 80]
    print("Original list ", lyst)

    # Get input for ascending or descending.
    order = str(input("\nDo you want the list in acsending order or descending order (up or down):  "))
    argument = order.lower()
    selectionSort(lyst, argument)

main()
