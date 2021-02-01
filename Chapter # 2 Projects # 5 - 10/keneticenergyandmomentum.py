"""
Program:  keneticenergyandmomentum.py
Author:  Chad Lister
Date:  12/13/2020

Computes an object's kenetic energy and momentum.
        
1. The inputs are:

         massInKilograms
         velocityInMetersPerSecond
         
2. Computations:

         momentum = massInKilograms * velocityInMetersPerSecond
         kenetic energy = (massInKilograms * velocityInMetersPerSecond ** 2) * .5
 
3. The outputs are:

        the object's momentum
        the object's kenetic energy
        
"""
               
# Request the inputs

massInKilograms = float(input("Please enter the object's mass in kilograms:  "))
velocityInMetersPerSecond = float(input("Please enter the object's velocity in meters per second:  "))

# Compute the object's momentum and kenetic energy

momentum = massInKilograms * velocityInMetersPerSecond
keneticEnergy = (massInKilograms * velocityInMetersPerSecond ** 2) * .5

# Display the objects momentum and kenetic energy

print("The object's momentum is:  ", momentum, ".")
print("The object's kenetic energy is:  ", keneticEnergy, ".")
