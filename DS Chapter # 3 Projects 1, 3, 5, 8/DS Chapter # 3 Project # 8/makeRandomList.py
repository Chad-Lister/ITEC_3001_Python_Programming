"""
Program: makeRandomList.py
Author:  Chad Lister
Date:  01/21/2021

DS Chapter # 3 Project # 8:

    State the computational complexity of the makeRandomList function
    using Big-O notation and justify your answer.

"""

import random
import time

def makeRandomList(size):

    lyst = []
    count = 0

    for count in range(size):

        while True:

            number = random.randint(1, size)

            if not number in lyst:

                lyst.append(number)
                count += 1
                break

    print(lyst)
    print("\nOperations:  ", count)

    return lyst

def main():
    """ The main function. """

    lyst = []
    start = time.time()

    size = 10
    makeRandomList(size)

    elapsed = round(time.time() - start, 3)

    print("Elapsed time:  ", elapsed, "\n")

    lyst = []
    start = time.time()

    size = 100
    makeRandomList(size)

    elapsed = round(time.time() - start, 3)

    print("Elapsed time:  ", elapsed, "\n")

    print("\nSince the operations are a square of the preceding ones, it is a quadratic functon.")
    print("Therefore the Big-O notations is n * n or n power 2.")


main()
