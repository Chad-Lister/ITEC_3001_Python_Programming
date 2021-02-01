"""
Program: book.py
Author:  Chad Lister
Date:  01/10/2021

This module defines the Book class and defines the interface used in a library class.

"""

class Book(object):
    """ Represents a book in a library. """
        
    def __init__(self, title, author, currentPatron, waitingList):
        """ Constructor. """
        self._title = title
        self._author = author
        self._currentPatron = currentPatron
        self._waitingList = waitingList
        
    def __str__(self):
        """ Returns the string values of books. """
        result = "\n\tTitle:    " + self._title + "\n\tAuthor:     " + self._author + "\n\tChecked Out To:     " + \
                 self._currentPatron
        return result

    def getTitle(self):
        """ Returns a book title. """
        return self._title

    def getAuthor(self):
        """ Returns the author. """
        return self._author

    def getCurrentPatron(self):
        """ Returns who the book is checked out too. """
        return self._currentPatron

    def getWaitingList(self):
        """ Returns the waiting list. """
        return self._waitingList

    def addToList(self, name):
        """ Adds a book to the list."""
        self._waitingList.append(name)
        return self._waitingList
