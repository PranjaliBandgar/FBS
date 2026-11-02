# 6.Write a Program to input two angles from user and find third 
# angle of the triangle.

#Taking inputs from user
angle1 = float(input('Enter first angle of triangle :'))
angle2 = float(input('Enter second angle of triangle :'))

# calculate sum of two angles
sum = angle1 + angle2

# calculate third angle subtracting 180 - sum of two angles
angle3 = 180 - sum

# print the third angle
print(f'Third angle of triangle is {angle3}')
