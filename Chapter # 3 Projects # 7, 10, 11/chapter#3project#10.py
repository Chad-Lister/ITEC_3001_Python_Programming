"""
Program:  chapter#3project#10.py
Author:  Chad Lister
Date: 12/15/2020

This program computes a payment schedule for the lifetime of a purchase on credit.
As per Chapter # 3 project # 10.  Assumed to be 12 month lifetime.

1.  The input is:

        purchasePrice

2.  Significant constants:

        ANNUAL_INTEREST_RATE
        MONTHLY_PAYMENT_RATE

3.  Computations:

        monthlyInterest = (outstandingBalance * ANNUAL_INTEREST_RATE) / 12
        principalPayment = (purchasePrice + downPayment) * MONTHLY_PAYMENT_RATE
        monthlyPayment = principalPayment + monthlyInterest
        endingBalance = outstandingBalance - principalPayment

4.  The display is in tabular format:

        month
        outstandingBalance
        monthlyInterest
        principalPayment
        monthlyPayment
        endingBalance
        
"""

# Initialize the constants

ANNUAL_INTEREST_RATE = .12
MONTHLY_PAYMENT_RATE = .05

# Accept the input from the user and calculate the down payment as a negative number

purchasePrice = float(input("Enter the purchase price: "))
downPayment = -(purchasePrice * .10)
print("Down payment:  " + " " * 6, "%10.2f" % downPayment)

# Initialize loop control and month (note:  downPayment is negative)

month = 1
outstandingBalance = purchasePrice + downPayment

# Display the header for the table including spacing

print()
print("%7s%20s%14s%14s%17s%17s" % \
      ("Month", "Current Balance",
       "Interest", "Principal", "Monthly Payment", "Ending Balance"))
print()

# Compute and display the results for each month

while outstandingBalance > 0.0:

    monthlyInterest = (outstandingBalance * ANNUAL_INTEREST_RATE) / 12
    principalPayment = (purchasePrice + downPayment) * MONTHLY_PAYMENT_RATE
    monthlyPayment = principalPayment + monthlyInterest
    endingBalance = outstandingBalance - principalPayment

    print("%-7d%20.2f%14.2f%14.2f%17.2f%17.2f" % \
          (month, outstandingBalance, monthlyInterest, principalPayment, monthlyPayment, endingBalance))

    outstandingBalance = endingBalance
    month += 1

   
