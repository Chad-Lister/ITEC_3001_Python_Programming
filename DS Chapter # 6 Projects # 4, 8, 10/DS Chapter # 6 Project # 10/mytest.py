"""
Program:  mytest.py
Author:  Chad Lister
Date:  01/26/2021

Test for DS Chapter # 6 Project # 10.

"""

from linkedbag import LinkedBag
#from new import LinkedBag

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
    print("\nBag error after remove 3:  ")
    b1.remove(3)

test(LinkedBag)
