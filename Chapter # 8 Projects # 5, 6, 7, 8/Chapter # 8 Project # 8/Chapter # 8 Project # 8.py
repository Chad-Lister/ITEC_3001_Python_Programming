"""
Program:  libraryManagement.py
Author:  Chad Lister
Date:  01/10/2021

This program runs the library management terminal.

"""

from book import Book
from patron import Patron
from library import Library

def main():
    """ The main function. """

    library = Library()
    option = 0

    # while not exit.
    while option != 6:

        print()
        print("***  Main Menu ***")
        print("_______________________________")
        print("\n\t1)  Check a book in")
        print("\t2)  Check a book out")
        print("\t3)  List patrons")
        print("\t4)  List books checked out")
        print("\t5)  List books on shelf")
        print("\t6)  Exit terminal")
        option = int(input("\n\tOption:  "))

        if option in range(1, 7):

            if option == 1:

                library.checkIn()

            if option == 2:

                library.checkOut()

            if option == 3:

                library.listPatrons()

            if option == 4:

                library.listBooks()

            if option == 5:

                library.listAvailable()
                
        else:
            print("\nInvalid Option!")
    print("\nHave a nice day!")

main()
