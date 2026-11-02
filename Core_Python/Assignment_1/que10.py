# 10.Write a program to calculate area of an equilateral triangle.
import math
# Taking input from user 
side = int(input('Enter the length of side:'))

# calculating area of equilateral triangle 
Area = (math.sqrt(3) / 4) * (side ** 2)

# print the area of equilateral triangle 
print(f'Area of equilateral triangle is {Area:.2f}')