"""
Program:  minutesinyear.py
Author:  Chad Lister
Date:  12/13/2020

This program computes the total minutes in a standard year and a leap year.

1. Significant constants:

        DAYS_IN_YEAR
        HOURS_IN_DAY
        MINUTES_IN_HOUR
 
2. Computations:

        minutesInYear = (MINUTES_IN_HOUR * HOURS_IN_DAY) * DAYS_IN_YEAR
        minutesInLeapYear = (MINUTES_IN_HOUR * HOURS_IN_DAY) * (DAYS_IN_YEAR + 1)
 
3. The output is:

        The minutes in a standard year
        The minutes in a leap yaer
        
"""

# Initialize the constants

DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

# Compute the minutes in a standard year

minutesInYear = (MINUTES_IN_HOUR * HOURS_IN_DAY) * DAYS_IN_YEAR
minutesInLeapYear= (MINUTES_IN_HOUR * HOURS_IN_DAY) * (DAYS_IN_YEAR + 1)
         
# Display the minutes in a standard year

print("There are", minutesInYear, "minutes in a standard year.")
print("There are", minutesInLeapYear, "minutes in a leap year.")
