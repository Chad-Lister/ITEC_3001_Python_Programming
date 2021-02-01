"""
Program:  library.py
Author:  Chad Lister
Date:  01/09/2021

This program defines the library class and interface used in Chapter # 8 Project # 8.

"""

from patron import Patron
from book import Book

class Library(object):
    """ Represents a library of patrons and books."""

    def __init__(self):

        books = []
        books.append(Book("The Hobbit", "J.R.R. Tolkien", "Doug Peters", ["Wendy Shale"]))
        books.append(Book("Greek Myths", "Troy Miller", "Bob Jones", []))
        books.append(Book("Python Programming", "Ken Lambert", "Wendy Shale", ["Bob Jones", "Doug Peters"]))
        books.append(Book("Introduction to Computers", "Ted Murphy", "Wendy Shale", []))
        books.append(Book("P.H.P. Basics", "Michael Smith", "Wendy Shale", ["Bob Jones"]))

        patrons = []
        patrons.append(Patron("Doug Peters", 1, ["The Hobbit"]))
        patrons.append(Patron("Bob Jones", 1, ["Greek Myths"]))
        patrons.append(Patron("Wendy Shale", 3, ["Python Programming", "Introduction to Computers", \
                                                 "P.H.P. Basics"]))

        availableBooks = []
        availableBooks.append(Book("A Time to Kill", "John Grisham", "", []))
        availableBooks.append(Book("East of Eden", "John Steinbeck", "", []))
        
        self._books = books
        self._patrons = patrons
        self._availableBooks = availableBooks

    def listAvailable(self):
        """ Lists books on shelf. """

        print()
        print("Books on shelf:")
        print()

        for book in self._availableBooks:
            print("\tTitle: ", book.getTitle())
            print("\tAuthor: ", book.getAuthor())
            print()

    def listBooks(self):
        """ Lists the books available. """

        print()
        print("Books:")
        
        for book in self._books:
            print(book)
            print("\tWaiting List: ", book.getWaitingList())
            #print()

    def listPatrons(self):
        """ Lists the patrons. """

        print()
        print("Patrons:")

        for patron in self._patrons:
            print(patron)
            print("\tBook List: ", patron.getBookList())
            #print()

    def checkIn(self):
        """ Checks a book in. """
        print()
        print("Cases must match.")
        print()
        name = input("Patron:  ")
        title = input("Book:  ")

        inList = True


        waiting = []
        newName = ""
        author = ""
        i = 0
        bookFound = False
        
        for book in self._books:
            bookTitle = book.getTitle()
            bookTitle = bookTitle.lower()
            if title.lower() == bookTitle:
                i = self._books.index(book)
                oldWait = book.getWaitingList()
                if len(oldWait) > 0:
                    newName = oldWait.pop()
                    for patron in self._patrons:
                        cname = patron.getName()
                        if newName == cname:
                            patron.addToList(title)
                            patron.addToCount()
                author = book.getAuthor()
                waiting = oldWait
                bookFound = True

        book = []
        newCount = 0
        p = 0
        patronFound = False
        
        for patron in self._patrons:
            patronName = patron.getName()
            patronName = patronName.lower()
            if name.lower() == patronName:
                bookList = patron.getBookList()
                if bookFound == True and inList == True:
                    bookIndex = patron.getBookList().index(title)
                    bookList.pop(bookIndex)
                book = bookList
                bookCount = patron.getBookCount()
                newCount = patron.getBookCount() - 1
                p = self._patrons.index(patron)
                patronFound = True

        if patronFound == True:

            if bookFound == True:
                
                if len(waiting) > 0:
                    self._patrons.pop(p)
                    self._books.pop(i)
                    self._patrons.append(Patron(name, newCount, book))
                    self._books.append(Book(title, author, newName, waiting))
                else:
                    self._patrons.pop(p)
                    self._books.pop(i)
                    self._patrons.append(Patron(name, newCount, book))
                    self._availableBooks.append(Book(title, author, newName, waiting))
            else:
                print("Book not found!")
        else:
            print("Patron not found!")

    def checkOut(self):
        """ Checks a book out. """

        print()
        print("Cases must match.")
        print()
        name = input("Patron:  ")
        title = input("Book Title:  ")

        bookAvailable = False
        bookFound = False
        waiting = []
        i = 0
        newName = ""
        author = ""

        for book in self._availableBooks:
            bookTitle = book.getTitle()
            if title == bookTitle:
                bookAvailable = True
                i = self._availableBooks.index(book)
                author = book.getAuthor()
                newName = name

        for book in self._books:
            bookTitle = book.getTitle()
            if title == bookTitle:
                bookFound = True
                i = self._books.index(book)
                author = book.getAuthor()
                newName = book.getCurrentPatron()
                oldWait = book.getWaitingList()
                waiting = book.addToList(name)

        patronFound = False
        bookList = []
        count = 0
        p = 0
        flag = False

        for patron in self._patrons:
            patronName = patron.getName()
            if patronName == name:
                newCount = patron.getBookCount() + 1
                if patron.checkCount(newCount) == True and bookAvailable == False:
                    patronFound = True
                    oldList = patron.getBookList()
                    bookList = oldList
                    p = self._patrons.index(patron)
                    count = patron.getBookCount()
                    print("\nPatron added to waiting list.")
                elif bookAvailable == True and patron.checkCount(newCount) == True:
                    bookList = patron.addToList(title)
                else:
                    count = patron.getBookCount()
                    flag = True
                    print("\nPatron is already at maximum books allowed!")

        if patronFound == True:

            if bookAvailable == True and bookFound == False:

                self._availableBooks.pop(i)
                self._patrons.pop(p)
                self._books.append(Book(title, author, newName, waiting))
                self._patrons.append(Patron(name, count, bookList))

            elif bookFound == True and bookAvailable == False:

                self._books.pop(i)
                self._patrons.pop(p)
                self._books.append(Book(title, author, newName, waiting))
                self._patrons.append(Patron(name, count, bookList))

            else:
                print("Book not found!")

        elif flag == False:
            print("Patron not found!")
