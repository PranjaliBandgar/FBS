# 9.Write a program to enter base and height of a triangle and find 
# its area.

# Taking inputs from users
base = float(input('Enter base of a triangle:'))
height = float(input('Enter height of a triangle'))

# Calculate area of triangle by using formula
# formula = (Base * Height) /2
Area = (base * height)/2

#print the area of triangle
print(f'The area of triangle is {Area}')