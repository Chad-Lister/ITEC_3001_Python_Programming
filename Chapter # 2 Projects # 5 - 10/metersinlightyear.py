"""
Program:  metersinlightyear.py
Author:  Chad Lister
Date:  12/13/2020

This program computes the meters light travels in a year (365 days).

1. Significant constants:

        METERS_PER_SECOND
        DAYS_IN_YEAR
        HOURS_IN_DAY
        MINUTES_IN_HOUR
        SECONDS_IN_MINUTE
 
2. Computations:

        lightYearInMeters = (((METERS_PER_SECOND * SECONDS_IN_MINUTE) * MINUTES_IN_HOUR)
                             * HOURS_IN_DAY) * DAYS_IN_YEAR
 
3. The output is:

        The distance in meters light travels in a year (365 days)
        
"""

# Initialize the constants

DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60
METERS_PER_SECOND = 3 * 10 ** 8
# METERS_PER_SECOND = 3 * 10e8  changes to regular notation

# Compute the distance light travels in meters in a year (365 days)

lightYearInMeters = (((METERS_PER_SECOND * SECONDS_IN_MINUTE) * MINUTES_IN_HOUR) * HOURS_IN_DAY) * DAYS_IN_YEAR
         
# Display the distance, in meters, light travels in a year (365 days)

print("Light travels", lightYearInMeters, "meters in a standard year (365 days).")
