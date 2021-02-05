"""
File: tokens.py

Tokens for processing expressions.

DS Chapter # 7 Project # 4:

    add the ^ operator to the expressions processed by the expression
    evaluator of the case study.
    
"""

class Token(object):

    UNKNOWN  = 0        # unknown
    
    INT      = 4        # integer
            
    MINUS    = 5        # minus    operator
    PLUS     = 6        # plus     operator
    MUL      = 7        # multiply operator
    DIV      = 8        # divide   operator
    # Added by Chad.
    XOR      = 9        # bianary xor????

    FIRST_OP = 5        # first operator code

    def __init__(self, value):
        if type(value) == int:
            self._type = Token.INT
        else:
            self._type = self._makeType(value)
        self._value = value

    def isOperator(self):
        return self._type >= Token.FIRST_OP

    def __str__(self):
        return str(self._value)
    
    def getType(self):
       return self._type
    
    def getValue(self):
       return self._value

    def _makeType(self, ch):
        if   ch == '*': return Token.MUL
        elif ch == '/': return Token.DIV
        elif ch == '+': return Token.PLUS
        elif ch == '-': return Token.MINUS
        # Added by Chad.
        elif ch == '^': return Token.XOR
        else:           return Token.UNKNOWN;

def main():
    # A simple tester program
    plus = Token("+")
    minus = Token("-")
    mul = Token("*")
    div = Token("/")
    # Added by Chad.
    xor = Token("^")
    unknown = Token("#")
    anInt = Token(34)
    print(plus, minus, mul, div, xor, unknown, anInt)

if __name__ == '__main__': 
    main()

