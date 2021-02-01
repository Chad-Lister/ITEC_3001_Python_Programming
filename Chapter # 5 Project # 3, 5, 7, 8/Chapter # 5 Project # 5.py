"""
Program:  decimalToRep.py
Author:  Chad Lister
Date:  12/21/2020

This program takes an integer and base input and uses several lookup tables to convert the integer to the base.
It should contain a main and several tests.

1.  Significant constants are:

        decimalToBinaryTable
        decimalToOctalTable
        decimalToHexTable

2.  Input is:

        the integer and a table

3.  Computation is:

        if base is 2.  For digits in integer's value lookup in decimalToBinaryTable and add to string.
        if base is 8.  For digits in integer's value lookup in decimalToOctalTable and add to string.
        if base is 16 ( 9 ?).  For digits in integer's value lookup in decimalToHexTable and add to string.

4.  Output is:

        the converted integer using the indicated base
        
"""

# Lookup tables

decimalToBinaryTable = {"0" : "00000000", "1" : "00000001", "2" : "00000010", "3" : "00000011", "4" : "00000100",
                        "5" : "00000101", "6" : "00000110", "7" : "00000111", "8" : "00001000", "9" : "00001001", "10" : "00001010",
                        "11" : " 00001011", "12" : "00001100", "13" : "00001101", "14" : "00001110", "15" : "00001111", "16" : "00010000", "17" : "00010001"}

decimalToOctalTable = {"0" : "0", "1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6", "7" : "7",
                       "8" : "10", "9" : "11", "10" : "12", "11" : "13", "12" : "14", "13" : "15", "14" : "16", "15" : "17", "16" : "20"}

decimalToHexTable = {"0" : "0", "1" : "01", "2" : "02", "3" : "03", "4" : "04",
                     "5" : "05", "6" : "06", "7" : "07", "8" : "08", "9" : "09",
                     "10" : "0A", "11" : "0B", "12" : "0C", "13" : "0D", "14" : "0E", "15" : "0F", "16" : "10", "17" : "11"}

# Main

def main():
    """ The programs main function. """
    
    print("For the decimal integer 12")
    print("Binary equivalent is:  ", convert("12", decimalToBinaryTable))
    print()

    print("For the decimal integer 10")
    print("Octal equivalent is:  ",convert("10", decimalToOctalTable))
    print()

    print("For the decimal integer 15")
    print("Hex equivalent is:  ", convert("15", decimalToHexTable))
    print()

# Conversion function

def convert(number, table):
    """ Converts an integer to the table equivalent. """

    value = ""
    digit = number
    value = table[digit] + value
        
    return value

main()
