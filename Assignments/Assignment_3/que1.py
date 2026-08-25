1. #1.Write a program to check if the given number is positive or 
#   negative.
num = int(input('Enter number:'))
if num > 0:
    print(f'{num} is positive number.')
elif num < 0:
    print(f'{num} is a negative number.')
else:
    print('Number is zero')