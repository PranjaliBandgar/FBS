# 7.Program to Find the Roots of a Quadratic Equation
import math
import cmath

#Taking inputs from user
a = float(input('Enter coefficient a:'))
b = float(input('Enter coefficient b:'))
c = float(input('Enter coefficient c:'))

# Quadtratic queation is ax**2 +bx + c =0
# calculate square root of b**2 -4ac
d = cmath.sqrt((b **2) -(4 * a * c))

# puting the of d in formula
root1 = (-b + (d) / (2 * a))
root2 = (-b -(d) / (2 * a))

# printing the roots
print(f'First root is {root1}')
print(f'Second root is {root2}')
    
