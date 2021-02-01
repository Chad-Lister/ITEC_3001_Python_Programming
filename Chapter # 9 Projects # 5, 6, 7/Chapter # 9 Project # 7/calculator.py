"""
Program:  calculator.py
Author:  Chad Lister
Date:  01/16/2021

This program defines the calculator class and interface for the calculatorview program.

"""

class Calculator():

    def __init__(self):
        """ Constructor. """

        self._result = 0


    def add(self, number1, number2):
        """ Adds 2 numbers. """

        self._result = number1 + number2

        return self._result

    def subtract(self, number1, number2):
        """ Subtracts 2 numbers. """

        self._result = number1 - number2

        return self._result

    def multiply(self, number1, number2):
        """ Multiplies 2 numbers. """

        self._result = number1 * number2

        return self._result

    def divide(self, number1, number2):
        """ Divides 2 numbers. """

        self._result = number1 / number2

        return self._result
