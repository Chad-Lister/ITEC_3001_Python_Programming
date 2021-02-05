"""
Program:  array.py
Author:  Chad Lister
Date:  01/22/2021

DS Chapter # 4 Project # 2:

    add preconditions to the _getitem and _setitem methods and raise
    an error if not satisfied.

"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""

        self._logicalSize = 0
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)
            self._logicalSize += 1

    def size(self):
        """ Returns the logical size of the array. """

        self._logicalSize = len(self._items)
        return self._logicalSize

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

        if 0 <= index < size():
            return self._items[index]
        else:
            raise IndexError(["Sequence index out of range."])
            return

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""

        if 0 <= index < size():
            self._items[index] = newItem
            return
        else:
            raise IndexError(["Sequence index out of range."])
            return
