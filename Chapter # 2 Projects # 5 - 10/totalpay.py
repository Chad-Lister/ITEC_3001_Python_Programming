"""
Program:  totalpay.py
Author:  Chad Lister
Date:  12/13/2020

This program computes an employee's total pay.

1. The inputs are:

        payRate
        totalHours
        overtimeHours
 
3. Computations:

        regularPay = payRate * totalHours
        overtimePay = (payRate * 1.5) * overtimeHours
        totalPay = regularPay + overtimePay

4. The output is:

        The employee's total pay

"""

# Request the inputs
   
payRate = float(input("Please enter the employee's hourly wage:  $ "))
totalHours = float(input("Please enter the employee's regular hours worked:  "))
overtimeHours = float(input("Please enter the employee's overtime hours, if any:  "))

# Compute the employee's total pay

regularPay = payRate * totalHours
overtimePay = (payRate * 1.5) * overtimeHours
totalPay = regularPay + overtimePay

# Display the employee's total pay

print("The employee's total pay is $", totalPay, ".")
