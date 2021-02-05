"""
Program:  mytest.py
Author:  Chad Lister
Date:  01/28/2021

Runs the tests for DS Chapter # 7 Project # 1.

"""
from linkedstack import LinkedStack
from arraystack import ArrayStack

def test(stackType):

    s = stackType()
    
    for i in range(15):
        s.push(i + 1)
    print("Stack loaded to 15 when 10 is default size:")
    print(s)

    for i in range(14):
        s.pop()
    print("\nStack after removing 14 items and new size:")
    print(s)
    print("Length =", len(s))
    b = stackType()
    print("\nEmpty stack error:")
    #b.pop()
    b.peek()
    print()

#test(ArrayStack)
test(LinkedStack)
