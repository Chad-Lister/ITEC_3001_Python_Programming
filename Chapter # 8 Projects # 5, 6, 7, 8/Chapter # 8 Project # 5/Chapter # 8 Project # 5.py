"""
Program:  bankManagerTerminal.py
Author:  Chad Lister
Date:  01/05/2021

This program runs a terminal for a bank manager, allowing them to add, delete
or edit an account defined in the bank class.  Instructors bank.py used.

1)  Input is:

        a menu choice

2)  Computations are:

        1 - add to bank
        2 - remove from bank
        3 - get old info, change and replace old
        4 - list bank
        5 - save to file
        6 - exit

3)  Output is:

        The main menu until exit
        
"""

from bank import Bank, SavingsAccount

def terminal():
    """ The terminal menu driver. """

    option = 0
    bank = Bank("bank.dat")

    # while not exit.
    while option != 6:

        print("***  Main Menu ***")
        print("_______________________________")
        print("\n\t1)  Add an account")
        print("\t2)  Delete an account")
        print("\t3)  Edit an account")
        print("\t4)  List bank entries")
        print("\t5)  Save to file")
        print("\t6)  Exit terminal")
        option = int(input("\n\tOption:  "))

        # add an account.
        if option == 1:

            print()
            name = str(input("Please enter account holder's name to add:  "))
            pin = str(input("Please enter their PIN:  "))
            balance = str(input("Please enter their initial balance:  "))
            bank.add(SavingsAccount(name, pin, balance))
            print()

        # delete an account.
        elif option == 2:

            pin = str(input("Please enter the PIN to remove:  "))
            bank.remove(pin)
            print()
            
        # edit an account.
        elif option == 3:

            newName = ""
            newBalance = ""

            print()
            oldPin = str(input("Please enter the PIN for the account:  "))
            original = bank.get(oldPin)
            oldName = SavingsAccount.getName(original)
            oldBalance = SavingsAccount.getBalance(original)
            print()
            print("Modifying original ...", original)
            nameChange = str(input("Change account holder's name (Y / N)?"))

            if nameChange.upper() == "Y":
                newName = str(input("Please enter the new name:  "))
            else:
                newName = oldName

            balanceChange = str(input("Change account balance (Y / N)?"))

            if balanceChange.upper() == "Y":
                newBalance = str(input("Please enter the new balance:  "))
            else:
                newBalance = oldBalance

            # remove and replace.
            bank.remove(oldPin)
            bank.add(SavingsAccount(newName, oldPin, newBalance))
            print()

        # print list.
        elif option == 4:
            print()
            print(bank)
            print()

        # save to file.
        elif option == 5:
            print()
            fileName = str(input("Please enter the file name to save as ..."))
            bank.save(fileName)
            print("File saved as", fileName)
            print()

    return

def main():
    """ The main function. """

    terminal()

    return

main()
