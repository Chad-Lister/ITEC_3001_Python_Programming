"""
Program:  patron.py
Author:  Chad Lister
Date:  01/10/2021

This program defines the Patron class and defines the interface used in a library class.

"""

class Patron():
    """ This class represents a library patron. """

    MAX_BOOK_COUNT = 3

    def __init__(self, name, bookCount, bookList):
        """ Constructor. """
        self._name = name
        self._bookCount = bookCount
        self._bookList = bookList
    
    def __str__(self):
        """ Returns the string values for patrons. """
        result = "\n\tName:    " + self._name + "\n\tBook Count:     " + str(self._bookCount)
        return result

    def getName(self):
        """ Returns the users name. """
        return self._name

    def getBookCount(self):
        """ Returns the number of books currently checked out. """
        return self._bookCount

    def getBookList(self):
        """ Returns the book list currently held by the user. """
        return self._bookList

    def checkCount(self, count):
        """ Checks if max count has been reached. """

        if count > Patron.MAX_BOOK_COUNT:
            return False
        else:
            return True

    def addToList(self, title):
        """ Adds a book to the list. """
        self._bookList.append(title)
        return self._bookList

    def addToCount(self):
        self._bookCount += 1
        return self._bookCount
