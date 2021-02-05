"""
Program:  mytest.py
Author: Chad Lister
Date:  01/25/2021

Tests my programs for DS Chapter # 5

"""

from arraysortedbag import ArraySortedBag

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973]
    print("The list of items added is:", lyst)
    b1 = bagType(lyst)
    print("\nOriginal Bag:")
    print(b1)
    b1.add(25)
    b1.add(2999)
    print("\nBag after adding 25 and 2999:")
    print(b1)
    b1.remove(1973)
    print("\nBag after removing 1973:")
    print(b1)

test(ArraySortedBag)
