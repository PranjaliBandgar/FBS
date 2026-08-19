# Find the volume of sphere.

import math

# Taking inputs from user
radius = float(input('Enter the radius of sphere:'))

# calculate the volume by using formula (volume = 4/3 * pi *radius **3)
volume = (4/3) * math.pi * radius ** 3

# print the volume of sphere 
print(f'The volume of sphere is {volume:.2f}')

