# 11. Find the area and circumference of circle.

import math

# taking inputs from user
radius = float(input('Enter the radius of circle'))

# calculate area using formula
area = math.pi * radius ** 2

# calculate circumference of circle
circumference = 2 * math.pi * radius

# print area and circumference
print(f'Area of circle is {area:.2f}')
print(f'Circumference of circle is {circumference:.2f}')