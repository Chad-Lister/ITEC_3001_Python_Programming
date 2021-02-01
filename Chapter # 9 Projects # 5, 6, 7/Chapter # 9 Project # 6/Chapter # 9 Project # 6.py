"""
Program:  mvc.py
Author:  Chad Lister
Date:  01/16/2021

This program runs a GUI for the program from Chapter # 3 Project # 10.  The TidBit Computer payment plan.
Using a seperate View and Model class.

"""

from tkinter import *

class View(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("TidBit Computers")
        self.master.geometry("640x580")
        self.grid()
        self._interestVar = DoubleVar()
        self._amountVar = DoubleVar()
        self._rate = 0
        self._price = 0
        self._out = 0.0
        self._current = 0.0
        self._down = 0.0
        self._model = None
        self._text = ""

        # Labels for entry fields.
        self._interestLabel = Label(self, text = "Annual Interest Rate:")
        self._interestLabel.grid(row = 0, column = 0)
        self._priceLabel = Label(self, text = "Purchase Price:")
        self._priceLabel.grid(row = 1, column = 0)

        # Entry fields.
        self._interestVar.set("")
        self._amountVar.set("")
        self._interestEntry = Entry(self, width = 10,
                                  textvariable = self._interestVar, 
                                  justify = CENTER)
        self._interestEntry.grid(row = 0, column = 1)


        self._amountEntry = Entry(self, width = 10,
                                  textvariable = self._amountVar, 
                                  justify = CENTER)
        self._amountEntry.grid(row = 1, column = 1)

        # Key event.
        self._amountEntry.bind("<KeyPress-Return>", lambda event: self._getTable())
    
    def _getTable(self):

        annualInterest = self._interestVar.get() / 100
        self._rate = annualInterest
        
        purchasePrice = self._amountVar.get()
        self._price = purchasePrice

        self._dataPane = Frame(self)
        self._dataPane.grid(row = 6, column = 0)
        self._model = Model(self._rate, self._price)
        self._text = Label(self._dataPane, text = "Month")
        self._text.grid(row = 6, column = 0)
        self._text = Label(self._dataPane, text = "Current Balance")
        self._text.grid(row = 6, column = 1)
        self._text = Label(self._dataPane, text = "Interest")
        self._text.grid(row = 6, column = 2)
        self._text = Label(self._dataPane, text = "Principal")
        self._text.grid(row = 6, column = 3)
        self._text = Label(self._dataPane, text = "Monthly Payment")
        self._text.grid(row = 6, column = 4)
        self._text = Label(self._dataPane, text = "Ending Balance")
        self._text.grid(row = 6, column = 5)

        month = 1
        r = 8
        self._down = self._model.getDownPayment()
        self._down = round(self._down, 2)
        self._current = self._price - self._down
        self._current = round(self._current, 2)
        principal = self._model.getPrincipal()
        principal = round(principal, 2)
        interest = (self._current * self._rate) / 12
        interest = round(interest, 2)
        monthly = principal + interest
        monthly = round(monthly, 2)
        end = self._current - principal
        end = round(end, 2)
        self._model.setCurrent(self._current)
        self._model.setOut(end)

        while self._current > 0:

            self._text = Label(self._dataPane, text = str(month))
            self._text.grid(row = r, column = 0)
            self._text = Label(self._dataPane, text = str(self._current))
            self._text.grid(row = r, column = 1)
            self._text = Label(self._dataPane, text = str(interest))
            self._text.grid(row = r, column = 2)
            self._text = Label(self._dataPane, text = str(principal))
            self._text.grid(row = r, column = 3)
            self._text = Label(self._dataPane, text = str(monthly))
            self._text.grid(row = r, column = 4)
            self._text = Label(self._dataPane, text = str(end))
            self._text.grid(row = r, column = 5)
            r += 1
            month += 1
            self._model.setOut(end)
            interest = self._model.getInterest(self._rate)
            interest = round(interest, 2)
            monthly = self._model.getMonthly()
            monthly = round(monthly, 2)
            end = self._model.getEnd()
            end = round(end, 2)
            self._current = self._current - principal
            self._current = round(self._current, 2)

        return

class Model(object):

    def __init__(self, rate, price):

        self._rate = rate
        self._price = price
        self._downPayment = 0.0
        self._out = 0.0
        self._current = 0.0
        self._interest = 0.0
        self._principal = 0.0
        self._monthly = 0.0
        self._ending = 0.0
        
    def getDownPayment(self):
        self._downPayment = self._price * .10
        return self._downPayment

    def getOut(self):
        self._out = self._ending
        return self._out

    def setOut(self, amount):
        self._out = amount
        return self._out

    def getCurrent(self):
        self._current = self._out
        return self._current

    def setCurrent(self, amount):
        self._current = amount
        return self._current

    def getInterest(self, rate):
        self._interest = (self._out * self._rate) / 12
        return self._interest

    def getPrincipal(self):
        MONTHLY_PAYMENT_RATE = .05
        self._principal = (self._price - self._downPayment) * MONTHLY_PAYMENT_RATE
        return self._principal

    def getMonthly(self):
        self._monthly = self._principal + self._interest
        return self._monthly

    def getEnd(self):
        self._ending = self._out - self._principal
        return self._ending

def main():

    initScreen = View()
    print("GUI started.")

main()
