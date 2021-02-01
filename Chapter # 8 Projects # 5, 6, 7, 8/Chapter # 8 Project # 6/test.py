"""
Program:  test.py
Author:  Chad Lister
Date:  01/09/2021

This program tests the Book and Patron classes.

"""

from book import Book
from patron import Patron

def testBook():
    """ Test the book class. """

    # book build
    books = []
    books.append(Book("The Hobbit", "J.R.R. Tolkien", "Doug", ["Wendy"]))
    books.append(Book("Greek Myths", "Troy Miller", "Bob", []))
    books.append(Book("Python Programming", "Ken Lambert", "Wendy", ["Bob", "Doug"]))
    books.append(Book("Introduction to Computers", "Ted Murphy", "Wendy", []))
    books.append(Book("P.H.P. Basics", "Michael Smith", "Wendy", ["Bob"]))

    print("Current Books:")
    print()
    for i in range(len(books)):
        print("\tTitle:  ", books[i].getTitle())
        print("\tAuthor:  ", books[i].getAuthor())
        print("\tChecked Out To:  ", books[i].getCurrentPatron())
        print("\tCurrent Waiting List:  ", books[i].getWaitingList())
        print()

def testPatron():
    """ Test the patron class. """

    # patron build
    patrons = []
    patrons.append(Patron("Doug Peters", 1, ["The Hobbit"]))
    patrons.append(Patron("Bob Jones", 1, ["Greek Myths"]))
    patrons.append(Patron("Wendy Shale", 3, ["Python Programming", "Introduction to Computers", \
                                             "P.H.P. Basics"]))

    print("Current Patrons:")
    print()
    for i in range(len(patrons)):
        print("\tName:  ", patrons[i].getName())
        print("\tBook Count:  ", patrons[i].getBookCount())
        print("\tBook List:  ", patrons[i].getBookList())
        print()

def main():

    testBook()
    testPatron()

main()
