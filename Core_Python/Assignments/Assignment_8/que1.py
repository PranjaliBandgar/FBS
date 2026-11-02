#1.Write a program to calculate area of rectangle

def area_of_rectangle(length,breadth):
    return length*breadth

length = float(input('Enter length of rectangle:'))
breadth = float(input('Enter breadth of rectangle:'))

area = area_of_rectangle(length,breadth)
print(f'The area of rectangle is:{area}')