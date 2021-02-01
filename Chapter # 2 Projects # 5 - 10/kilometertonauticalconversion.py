"""
Program:  kilometertonauticalconversion.py
Author:  Chad Lister
Date:  12/13/2020

This program converts kilometers to nautical miles.

1. The inputs are:

        totalKilometers

2. Computations:

        totalNautical = totalKilometers * .53996

        1 km = 0.53996 nautical
        1 nautical = 1.852 km

3. The outputs are:

        The total nautical miles for the number of kilometers entered

"""

# Request the inputs

totalKilometers = float(input("Please enter the number of kilometers to convert to nautical miles:  "))

# Compute the 

totalNautical = totalKilometers * 0.539956803

# Display the 

print("There are", totalNautical, "nautical miles in", totalKilometers, "kilometers.")
