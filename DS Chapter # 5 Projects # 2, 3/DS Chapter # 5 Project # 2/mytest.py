"""
Program:  mytest.py
Author: Chad Lister
Date:  01/25/2021

Tests my programs for DS Chapter # 5

"""

from arraybag import ArrayBag

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973, 2, 88, 1590, 9999, 21200, 5]
    print("The list of items added is:", lyst)
    b1 = bagType(lyst)
    print("\nOriginal Bag:")
    print(b1)
    print("Length of original bag:  ", len(b1))
    b1.add(25)
    b1.add(2999)
    print("\nBag after adding 25 and 2999:")
    print(b1)
    print("Length of bag:  ", len(b1))
    b1.remove(1973)
    print("\nBag after removing 1973:")
    print(b1)
    print("Length of bag:  ", len(b1))

test(ArrayBag)
