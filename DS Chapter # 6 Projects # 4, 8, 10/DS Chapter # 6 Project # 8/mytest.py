"""
Program:  mytest.py
Author:  Chad Lister
Date:  01/26/2021

Test for DS Chapter # 6 Project # 8.

"""

from arraybag import ArrayBag

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973, 55, 7025]
    print("The list of items added is:", lyst)
    b1 = bagType(lyst)
    print("\nOriginal bag:  ")
    print(b1)
    print("\nBag after remove 55:  ")
    b1.remove(55)
    print(b1)
    print("\nBag after add 25:  ")
    b1.add(25)
    print(b1)

test(ArrayBag)
