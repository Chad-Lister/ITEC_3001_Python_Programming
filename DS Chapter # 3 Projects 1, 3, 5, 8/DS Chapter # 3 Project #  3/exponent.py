"""
Program:  exponent.py
Author:  Chad Lister
Date: 01/21/2021

DS Chapter # 3 Project # 3:

    Define an expo function that mimicks Python's pow function.  Taking 2 inputs
    and state it's computaional complexity using Big-O notation.


"""

def main():
    """ The main function. """

    # Get inputs.
    number = int(input("Please enter an integer number:  "))
    exp = int(input("Please enter it's exponent (nonnegative integers only.):  "))

    def expo(number, exp):

        i = 0
        power = 1

        while exp > 0:

            power *= number
            i += 1
            exp -= 1
            
        print("\nThe result of the inputs equals", power)
        print("The computational complexity of this algorithm is O(2ⁿ).")
        print("With a workload that can exceed charts.  Currently ", i, "iterations.")
    

    expo(number, exp)
   
main()         
