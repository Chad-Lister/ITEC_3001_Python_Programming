"""
Program:  array.py
Author:  Chad Lister
Date:  01/22/2021

DS Chapter # 4 Project # 3:

    add the methods grow and shrink to the array class.  Make sure that the physical
    size does not shrink below the init capacity and that the array fills the cells if increased.

Note:  The shrink method never executes because the constructor fills the array
       at instantiation.

"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""

        self._logicalSize = 0
        self._capacity = capacity
        self._fillValue = fillValue
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)
            self._logicalSize += 1

    def size(self):
        """ Returns the logical size of the array. """

        self._logicalSize = len(self._items)
        return self._logicalSize

    def shrink(self):
        """ Shrinks the array if larger than initial capacity.

        ***  Never executes since logical is always equal to length ***

        """

        logicalSize = self._logicalSize
        length = len(self._items)

        if logicalSize <= length // 4 and length >= self._capacity * 2:
            temp = Array(length // 2)
            for i in range(logicalSize):
                temp[i] = self._items[i]
                logicalSize -= 1
            self._items = temp
            self._logicalSize = logicalSize

        return

    def grow(self):
        """  Grows the array when capacity is reached. """

        logicalSize = self._logicalSize
        length = len(self._items)

        if logicalSize == length:
            temp = Array(length * 2)
            for i in range(logicalSize):
                temp[i] = self._items[i]
                
            # fill rest with fill value.
            newLogical = logicalSize
            for f in range(logicalSize, len(temp)):
                temp[f] = self._fillValue
                newLogical += 1
            self._items = temp
            self._logicalSize = newLogical

        return

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""

        size = len(self._items)

        if 0 <= index < size:
            return self._items[index]
        else:
            raise IndexError(["Sequence index out of range."])
            return

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""

        size = len(self._items)

        if 0 <= index < size:
            self._items[index] = newItem
            return
        else:
            raise IndexError(["Sequence index out of range."])
            return

# For testing
##def main():
##
##    a = Array(10, 1)
##    print(a)
##    size = len(a)
##    a.grow()
##    print(a)
##    newS = len(a)
##    a.grow()
##    a.grow()
##    t = len(a)
##    #a.grow()
##    a.shrink()
##    print(a)
##    sh = len(a)
##    print(size, " ", newS, " ", t, " ", sh)
##
##main()
