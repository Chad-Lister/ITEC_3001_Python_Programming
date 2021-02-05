"""
Program:  modelview.py
Author:  Chad Lister
Date:  01/31/2021

This program defines the view for the PFEvaluatorModel class.

DS Chapter # 7 Project # 4:

    add the ^ operator to the expressions processed by the expression
    evaluator of the case study.

"""

from scanner import Scanner
from model import *


def main():
    """ The main function. """

    # Main display loop.
    while True:

        # String variable.
        st = ""

        sourceStr = input("\nEnter an expression: ")
        if sourceStr == "": break
        scanner = Scanner(sourceStr)
        while scanner.hasNext():
            st += str(scanner.next())

        print("\nPrefix expression is", st)

        # String variables.
        temp2 = ""
        temp = ""
        temp3 = ""

        # Divide string into digits and operators.
        for i in range(len(st)):
            c = st[i]
            b = c.isdigit()

            # Add to digit string.
            if b == True:
                temp += c

            # Add to operator string and pad digit string.
            else:
                temp2 = " " + c + " " + temp2
                temp += " "

        # Add digit and operator string.
        temp3 = temp + temp2

        print("\nPostfix expression is", temp3)

        # Make PFEvaluatorModel and pass string to evaluate.
        m = PFEvaluatorModel()
        r = m.evaluate(temp3)
        print("\nEvaluates to:  ", r)

main()
