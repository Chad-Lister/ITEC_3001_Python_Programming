"""
File: arraystack.py
Author: Ken Lambert
Date:  01/28/2021

DS Chapetr # 7 Project # 1:

    Complete and test the linked and array implementations of the stack collection.
    Verify that exceptions are raised when preconditions are violated and that
    the array-based implementation adds or removes storage as needed.
    
"""

from arrays import Array
from abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    """An array-based stack implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    # Modified by Chad to test the precondition.
    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""

        if self.isEmpty():
            raise KeyError("Array Stack is currently empty.")
        return self._items[len(self) - 1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

    # Modified by Chad to grow if necessary.
    def push(self, item):
        """Inserts item at top of the stack."""

        # If already at default capacity, make a tempStack twice as long.
        if self._size == ArrayStack.DEFAULT_CAPACITY:

            tempStack = Array(ArrayStack.DEFAULT_CAPACITY * 2)
            i = 0
            # Copy self._items to tempStack and copy tempStack to self._items.
            for i in range(len(self)):
                tempStack[i] = self._items[i]
            self._items = tempStack
            
        self._items[len(self)] = item
        self._size += 1

    # Modified by Chad to check Preconditions and shrink if necessary.
    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""

        # Check if empty.
        if self.isEmpty():
            raise KeyError("Array Stack is currently empty.")

        oldItem = self._items[len(self) - 1]
        self._size -= 1

        # To simplify check.
        length = self._items[len(self)]
        if self._size <= length // 4 and length >= ArrayStack.DEFAULT_CAPACITY:

            # make a tempStack at half capacity and copy back to self._items.
            tempStack = Array(ArrayStack.DEFAULT_CAPACITY //2)
            i = 0
            for i in range(len(self)):
                tempStack[i] = self._items[i]

            self._items = tempStack
            
        return oldItem
        
