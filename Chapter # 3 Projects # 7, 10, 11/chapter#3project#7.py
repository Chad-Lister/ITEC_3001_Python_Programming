"""
Program: chapter#3project#7.py
Author: Chad Lister
Date:  12/14/2020

This program displays a salary schedule, in tabular format, for teachers in a school district.

1. The inputs are:

       startingSalary
       percentageIncrease
       numberOfYears

2. The report is displayed in tabular form with a header.

3. Computations and outputs:

       for each year
          print a formatted row listing  of year and salary for year upt o 10 years 
       
4. Display is:

        The salary schedule in tabular form
        
"""

# Accept the inputs from the user

baseSalary = float(input("Enter the beginnng salary: "))
years = int(input("Enter the number of years for the schedule (10 max): "))

# Test year input (10 year max)
if years > 10 or years < 1:
    print("Years must be between 1 and 10 for schedule.")
    years = int(input("Enter the number of years for the schedule (10 max): "))

    # If not 1 - 10 again
    while years > 10 or years < 1:
        years = int(input("Enter the number of years for the schedule (10 max): "))

percentageIncrease = int(input("Enter the yearly increase rate as a %: "))
print()

# Convert the percentage increase to a decimal number and initialize increase amount

percentageIncrease = percentageIncrease / 100
increase = 0.0

# Display the header for the table and space afterwards

print("%-6s%15s" % ("Year", "Yearly Salary"))
print()

# Compute and display the results for each year

for year in range(1, years + 1):
    increase = baseSalary * percentageIncrease
    print("%-6d%15.2f" % (year, baseSalary))
    baseSalary += increase

   
   
