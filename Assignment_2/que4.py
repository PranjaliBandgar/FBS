# 4.WAP to calculate area of triangle and rectangle

# Taking inputs from user 
# Triangle (Base and height)
base = int(input('Enter the base of triangle:'))
height = int(input('Enter the height of triangle:'))

Area_of_triangle = (base * height) /2

print(f'The area of triangle is {Area_of_triangle}')

# Rectangle (Length and Breadth)
length = int(input('Enter the length of rectangle:'))
breadth = int(input('Enter the breadth of rectangle:'))

Area_of_rectangle = length * breadth

print(f'The area of rectangle is {Area_of_rectangle}')
