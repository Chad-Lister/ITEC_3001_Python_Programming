"""
Program:  chapter#3project#11.py
Author:  Chad Lister
date: 12/15/2020

This program demonstrates the futility of playing the game Lucky Sevens.

1. The input is:

       initialPot

2. The report is displayed in tabular form with a header:

        initialPot
        balance
        roll

3. Computations and outputs:

        balance = initialPot
        roll = 1
        gain = 4
        loss = 1
        maxBalance = 0
        
        while balance > 1:
           dice1 = random.randint(1, 6)
           dice2 = random.randint(1, 6)
           total = dice1 + dice2

           if total == 7:
              balance = balance + gain
              maxBalance = balance
              roll +=

            else:
            balance = balance - loss
            roll +=
       
4. The output is:

        The initial pot + number of rolls + maxBalance
"""

import random

# Get user's initial pot or investment

initialPot = int(input("Please enter how much you wish to put in the pot:  "))

# Initialize variables

balance = initialPot
roll = 1
gain = 4
loss = 1
maxBalance = 0

# Compute rolls, balance, maxBalance until balance is 0

while balance > 0:
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    if total == 7:
        balance += gain
        maxBalance = balance
        roll += 1
    else:
        balance -= loss
        roll += 1

# Display results.

print("Initial investment =", initialPot)
print("Rolls until break or 0 balance =", roll)
print("Maximum balance in pot =", maxBalance)
