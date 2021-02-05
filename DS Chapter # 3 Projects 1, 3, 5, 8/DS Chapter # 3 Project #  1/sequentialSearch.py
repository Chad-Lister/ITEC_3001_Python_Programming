"""
Program:  sequentialsearch.py
Author:  Chad Lister
Date:  01/21/2021

DS Chapter # 3 Project # 1:

    Define a modified sequential search algorithm, and state it's complexity
    For worst, best, and average using Big-O notaion.

"""

def main():
    """ The main function. """

    # iteration counter.
    position = 1

    lyst = [1, 3, 6, 9, 4]
    print("For the list of", lyst)
    print("Target for Worst-Case is 4.")
    target = 4

    def sequentialSearch(target, lyst):

        position = 0
        while position < len(lyst):
            if target == lyst[position]:
                return position
            position += 1
        return -1
    
    position += sequentialSearch(target, lyst)

    print("The Worst-Case performance of the sequential search is O(n).")
    print("With ", position, "number of iterations.\n")

    print("For the list of", lyst)
    print("Target for Average-Case is 6.")
    target = 6
    position = 1

    position += sequentialSearch(target, lyst)

    print("The Average-Case performance of the sequential search is still O(n).")
    print("With ", position, "number of iterations.\n")

    print("For the list of", lyst)
    print("Target for Best-Case is 1")
    target = 1
    position = 1

    print("The Best-Case performance of the sequential search is O(1), ie; O(n).")
    print("With ", position, "number of iterations.")

main()
