#2.Write a program to calculate area of circle
import math
def area_of_circle(radius):
    return math.pi * (radius * radius)
radius = float(input('Enter radius of circle:'))

area = area_of_circle(radius)
print(f'Area of circle is: {area:.2f}')