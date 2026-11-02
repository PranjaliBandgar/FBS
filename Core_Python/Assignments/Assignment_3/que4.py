#4. Write a program to input all sides of a triangle and check 
#   whether triangle is valid or not

a = float(input('Enter length of side a:'))
b = float(input('Enter length of side b:'))
c = float(input('Enter length of side c:'))

if a + b > c and b + c > a and a + c > b:
    print(f'Triangle is valid.')
else:
    print(f'Triangle is not valid.')