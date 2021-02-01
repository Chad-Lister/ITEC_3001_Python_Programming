"""
Program:  calculatorGUI.py
Author:  Chad Lister
Date:  01/16/2021

This program runs a GUI for a simple calculator.

"""

from tkinter import *
from calculator import Calculator

class CalculatorGUI(Frame):

    def __init__(self, calculator):

        # Create the main frame
        Frame.__init__(self)
        self.master.title("Calculator")
        self.master.geometry("300x300")
        self.master.resizable(0, 0)
        self.grid()
        self._calculator = Calculator()
        self._displayVar = StringVar()
        self._string = ""
        self._stringTemp = ""
        self._result = 0
        self._addFlag = False
        self._subFlag = False
        self._multFlag = False
        self._divFlag = False
        
        # Create the nested frame for the display and add widget.
        self._displayPane = Frame(self)
        self._displayPane.grid(row = 0, column = 0)
        self._display = Entry(self._displayPane, textvariable = self._displayVar, justify = LEFT)
        self._display.grid(row = 0, column = 1)

        # Create the nested frame for the button pane and widgets.
        self._buttonPane = Frame(self)
        self._buttonPane.grid(row = 1, column = 0)

        #first row.
        self._button7 = Button(self._buttonPane, text = "7", padx = 15, pady = 15, command = self._add7)
        self._button8 = Button(self._buttonPane, text = "8", padx = 15, pady = 15, command = self._add8)
        self._button9 = Button(self._buttonPane, text = "9", padx = 15, pady = 15, command = self._add9)
        self._button7.grid(row = 0, column = 0)
        self._button8.grid(row = 0, column = 1)
        self._button9.grid(row = 0, column = 2)

        # second row.
        self._button4 = Button(self._buttonPane, text = "4", padx = 15, pady = 15, command = self._add4)
        self._button5 = Button(self._buttonPane, text = "5", padx = 15, pady = 15, command = self._add5)
        self._button6 = Button(self._buttonPane, text = "6", padx = 15, pady = 15, command = self._add6)
        self._button4.grid(row = 1, column = 0)
        self._button5.grid(row = 1, column = 1)
        self._button6.grid(row = 1, column = 2)

        # third row.
        self._button1 = Button(self._buttonPane, text = "1", padx = 15, pady = 15, command = self._add1)
        self._button2 = Button(self._buttonPane, text = "2", padx = 15, pady = 15, command = self._add2)
        self._button3 = Button(self._buttonPane, text = "3", padx = 15, pady = 15, command = self._add3)
        self._button1.grid(row = 2, column = 0)
        self._button2.grid(row = 2, column = 1)
        self._button3.grid(row = 2, column = 2)

        # fourth row.
        self._button0 = Button(self._buttonPane, text = "0", padx = 58, pady = 15, command = self._add0)
        self._button0.grid(row = 3, column = 0, columnspan = 3)

        # Create the nested frame for the command pane and widgets.
        self._commandPane = Frame(self)
        self._commandPane.grid(row = 0, column = 4)
        self._buttonPlus = Button(self._buttonPane, text = "+", padx = 15, pady = 15, command = self._plus)
        self._buttonMinus = Button(self._buttonPane, text = "-", padx = 15, pady = 15, command = self._minus)
        self._buttonMult = Button(self._buttonPane, text = "*", padx = 15, pady = 15, command = self._multiply)
        self._buttonDiv = Button(self._buttonPane, text = "/", padx = 15, pady = 15, command = self._divide)
        self._buttonC = Button(self._buttonPane, text = "C", padx = 15, pady = 42, command = self._clear)
        self._buttonEQ = Button(self._buttonPane, text = "=", padx = 15, pady = 42, command = self._equals)
        self._buttonPlus.grid(row = 0, column = 4)
        self._buttonMinus.grid(row = 1, column = 4)
        self._buttonMult.grid(row = 2, column = 4)
        self._buttonDiv.grid(row = 3, column = 4)
        self._buttonC.grid(row = 0, column = 5, rowspan = 2)
        self._buttonEQ.grid(row = 2, column = 5, rowspan = 2)
    
    # Event handlers.

    def _plus(self):
        """ If not blank set add flag. """

        if len(self._string) == 0:
            self._displayVar.set("ERROR")
            return
        
        else:
            self._stringTemp = self._string
            self._string = ""
            self._addFlag = True
            self._displayVar.set(self._stringTemp)

    def _minus(self):
        """ If not blank set sub flag. """

        if len(self._string) == 0:
            self._displayVar.set("ERROR")
            return
        
        else:
            self._stringTemp = self._string
            self._string = ""
            self._subFlag = True
            self._displayVar.set(self._stringTemp)

    def _multiply(self):
        """ If not blank set mult flag. """

        if len(self._string) == 0:
            self._displayVar.set("ERROR")
            return
        
        else:
            self._stringTemp = self._string
            self._string = ""
            self._multFlag = True
            self._displayVar.set(self._stringTemp)

    def _divide(self):
        """ If number isn't blank set div flag. """

        if len(self._string) == 0:
            self._displayVar.set("ERROR")
            return
        
        else:
            self._stringTemp = self._string
            self._string = ""
            self._divFlag = True
            self._displayVar.set(self._stringTemp)

    def _equals(self):
        """ Passes 2 numbers to the calculator method.  Receives the result. """

        if self._addFlag == True and len(self._string) > 0:
            self._result = self._calculator.add(int(self._stringTemp), int(self._string))
            self._addFlag = False

        elif self._subFlag == True and len(self._string) > 0:
            self._result = self._calculator.subtract(int(self._stringTemp), int(self._string))
            self._subFlag = False

        elif self._multFlag == True and len(self._string) > 0:
            self._result = self._calculator.multiply(int(self._stringTemp), int(self._string))
            self._multFlag = False

        elif self._divFlag == True and len(self._string) > 0:

            # Divide by zero error.
            if self._string == "0":
                self._displayVar.set("ERROR")
                self._string = ""
                self._stringTemp = ""
                self._result = 0
                return
            
            self._result = self._calculator.divide(int(self._stringTemp), int(self._string))
            self._divFlag = False

        self._displayVar.set(str(self._result))
        self._string = ""
        self._stringTemp = ""
        self._result = 0

    def _clear(self):
        """ Clears the calculator. """

        self._displayVar.set("")
        self._string = ""
        self._stringTemp = ""
        self._result = 0
        self._addFlag = False
        self._subFlag = False
        self._multFlag = False
        self._divFlag = False
        
    def _add1(self):
        """ Adds 1 to the display. """
        self._string += "1"
        self._displayVar.set(self._string)

    def _add2(self):
        """ Adds 2 to the display. """
        self._string += "2"
        self._displayVar.set(self._string)

    def _add3(self):
        """ Adds 3 to the display. """
        self._string += "3"
        self._displayVar.set(self._string)

    def _add4(self):
        """ Adds 4 to the display. """
        self._string += "4"
        self._displayVar.set(self._string)

    def _add5(self):
        """ Adds 5 to the display. """
        self._string += "5"
        self._displayVar.set(self._string)

    def _add6(self):
        """ Adds 6 to the display. """
        self._string += "6"
        self._displayVar.set(self._string)
        
    def _add7(self):
        """ Adds 7 to the display. """
        self._string += "7"
        self._displayVar.set(self._string)

    def _add8(self):
        """ Adds 8 to the display. """
        self._string += "8"
        self._displayVar.set(self._string)

    def _add9(self):
        """ Adds 9 to the display. """
        self._string += "9"
        self._displayVar.set(self._string)
    
    def _add0(self):
        """ Adds 0 to the display. """
        self._string += "0"
        self._displayVar.set(self._string)

def main():
    """ The main function. """

    calculator = Calculator()
    print("Calculator started.")
    CalculatorGUI(calculator).mainloop()

main()
