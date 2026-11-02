#5.Write a program to check whether the triangle is equilateral, 
# isosceles or scalene triangle.

# Equilateral triangle = all sides are equal (a == b == c)
# Isosceles triangle =  any Two side are equal (a==b) or (b==c) or (a==c)
# scalene triangle = All sides are different

a = float(input('Enter length of side a:'))
b = float(input('Enter length of side b:'))
c = float(input('Enter length of side c:'))

if (a + b > c) and (b + c > a) and (a + c > b):
    if (a == b == c):
        print(f'The triangle is equilateral triangle.')
    elif (a == b) or (b == c) or (c == a):
        print(f'The triangle is isosceles triangle.')
    else:
        print(f'The triangle is scalene triangle.')
else:
    print(f'Triangle is not formad.')