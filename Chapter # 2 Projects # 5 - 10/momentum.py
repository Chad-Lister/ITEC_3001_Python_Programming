"""
Program:  momentum
Author:  Chad Lister
Date:  12/13/2020

Computes an objects momentum.

1. The inputs are:

         massInKilograms
         velocityInMetersPerSecond
         
2. Computations:

         momentum = massInKilograms * velocityInMetersPerSecond
 
3. The outputs are:

        the objects momentum
        
"""

# Request the inputs

massInKilograms = float(input("Please enter the object's mass in kilograms:  "))
velocityInMetersPerSecond = float(input("Please eneter the object's velocity in meters per second:  "))

# Compute the object's momentum

momentum = massInKilograms * velocityInMetersPerSecond
         
# Display the object's momentum

print("The object's momentum is:  ", momentum, ".")
