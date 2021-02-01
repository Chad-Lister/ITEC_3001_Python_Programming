"""
Program:  bankManager.py
Author:  Chad Lister
Date: 01/12/2021

This module defines a GUI-based Bank Manager class and its application using the book's Bank class.

"""

from bank import Bank, SavingsAccount
from tkinter import *  

class BankManager(Frame):
    """This class represents GUI-based Bank Manager Terminal. """

    def __init__(self, bank, sortedPins):
        """Initialize the frame, its grid, and the data model."""
        Frame.__init__(self)
        self.master.title("Bank Manager") 
        self.grid()
        self.master.geometry("525x175")
        self._bank = bank
        self._sortedPins = sortedPins
        self._account = None
        self._listLen = len(sortedPins) - 1
        self._index = 0
        self._nameVar = StringVar()
        self._pinVar = StringVar()
        self._balanceVar = DoubleVar()
        self._messageVar = StringVar()
        self._flag = None

        # Buttons.
        self._previousButton = Button(self, text = "<< Previous",
                                      command = self._previous,
                                      state  = NORMAL)
        self._previousButton.grid(row = 4, column = 0)
        self._nextButton = Button(self, text = "Next >>",
                                  command = self._next,
                                  state = NORMAL)
        self._nextButton.grid(row = 4, column = 2)

        # Initialize fields.
        self._login(self._sortedPins[0])

        # Labels for entry fields.
        self._nameLabel = Label(self, text = "Name")
        self._nameLabel.grid(row = 0, column = 0)
        self._pinLabel = Label(self, text = "PIN")
        self._pinLabel.grid(row = 1, column = 0)
        self._balanceLabel = Label(self, text = "Balance")
        self._balanceLabel.grid(row = 2, column = 0)
        self._messageLabel = Label(self, text = "Message")
        self._messageLabel.grid(row = 3, column = 0)

        # Entry fields.
        self._nameEntry = Entry(self, width = 30,
                                textvariable = self._nameVar, 
                                justify = CENTER)
        self._nameEntry.grid(row = 0, column = 1, pady = 10)
        self._pinEntry = Entry(self, width = 30,
                               textvariable = self._pinVar, 
                               justify = CENTER)
        self._pinEntry.grid(row = 1, column = 1)
        self._amountEntry = Entry(self, width = 30,
                                  textvariable = self._balanceVar, 
                                  justify = CENTER)
        self._amountEntry.grid(row = 2, column = 1)
        self._messageEntry = Entry(self, width = 30,
                                  textvariable = self._messageVar, 
                                  justify = CENTER)
        self._messageEntry.grid(row = 3, column = 1)

        self._addButton = Button(self, text = "Add",
                                 command = self._add)
        self._addButton.grid(row = 0, column = 2)
        self._addButton["state"] = NORMAL
        self._removeButton = Button(self, text = "Remove",
                                    command = self._remove)
        self._removeButton.grid(row = 1, column = 2)
        self._removeButton["state"] = NORMAL
        self._editButton = Button(self, text = "Update Edit",
                                    command = self._edit)
        self._editButton.grid(row = 2, column = 2)
        self._saveButton = Button(self, text = "Update Account",
                                   command = self._update)
        self._saveButton.grid(row = 3, column = 2)
        self._saveButton["state"] = NORMAL

    # Event-handling methods

    def _previous(self):
        """ Get previous account."""

        if self._index == 0:
            self._index = self._listLen
        elif self._index > 0:
            self._index -= 1

        self._login(self._sortedPins[self._index])

        return

    def _next(self):
        """ Get next account. """

        if self._index == self._listLen:
            self._index = 0
        elif self._index < self._listLen:
            self._index += 1

        self._login(self._sortedPins[self._index])

        return

    def _add(self):
        """ Adds an account using PIN as key. """

        self._messageVar.set("Enter account and press update account.")
        self._nameVar.set("")
        self._pinVar.set("")
        self._balanceVar.set(0.0)

        self._flag = True

        return

    def _remove(self):
        """ Removes an account from the bank. """

        self._messageVar.set("Enter PIN and press update account.")
        self._nameVar.set("")
        self._pinVar.set("")
        self._balanceVar.set(0.0)

        self._flag = False

        return

    def _edit(self):
        """ Edits an account. """

        name = self._nameVar.get()
        pin = self._pinVar.get()
        balance = self._balanceVar.get()

        self._bank.remove(pin)

        self._bank.add(SavingsAccount(name, pin, balance))
        self._messageVar.set("Account edited.")

        return

    def _update(self):
        """ Saves the account. """

        if self._flag == True:
            name = self._nameVar.get()
            pin = self._pinVar.get()
            balance = self._balanceVar.get()
            self._bank.add(SavingsAccount(name, pin, balance))
            self._sortedPins.append(pin)
            self._listLen += 1
            self._index = self._listLen
            self._messageVar.set("Account created.")
            self._flag = None
            self._sortedPins.sort()
            #rpin = 0
            #self._reset(self._sortedPins[rpin])

        elif self._flag == False:
            self._nameVar.set("*****")
            self._balanceVar.set("*****")
            pin = self._pinVar.get()
            self._bank.remove(pin)
            i = self._sortedPins.index(pin)
            self._sortedPins.pop(i)
            self._listLen -= 1
            self._index = self._listLen
            self._messageVar.set("Account removed.")
            self._flag = None
        
        return

##    def _reset(self, pin):
##        """ Resets the fields to first account."""
##
##        self._account = self._bank.get(pin)
##        if self._account:
##            name = self._account.getName()
##            pin = self._account.getPin()
##            balance = self._account.getBalance()
##            self._nameVar.set(name)
##            self._pinVar.set(pin)
##            self._balanceVar.set(balance)
##            self._messageVar.set("Welcome!")
##
##        return

    def _login(self, pin):
        """ Initializes the fields to first of sorted list. """
        
        self._account = self._bank.get(pin)
        if self._account:
            name = self._account.getName()
            pin = self._account.getPin()
            balance = self._account.getBalance()
            self._nameVar.set(name)
            self._pinVar.set(pin)
            self._balanceVar.set(balance)
            self._messageVar.set("Welcome!")

# Top-level functions
def main():
    """Instantiate a bank and use it in an ATM."""
    bank = Bank("bank.dat")
    print("The bank has been loaded")

    sortedPins = []
    sortedPins = bank.getPins()
    print("The pins have been sorted.")

    bankManager = BankManager(bank, sortedPins)
    print("Running the GUI")
    bankManager.mainloop()
    
    bank.save()  
    print("The bank has been updated")

def createBank(number = 0):
    """Saves a bank with the specified number of accounts.
    Used during testing."""
    bank = Bank()
    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i),
                                str(1000 + i),
                                100.00))
    bank.save("bank.dat")

main()
