# 7.Write a program to find sum of digits of a number.

def sum_of_digits(num):
    total = 0

    for digit in str(num):
        total = total + int(digit)
    return total
num = int(input('Enter the number:'))

result = sum_of_digits(num)
print(f'Number: {num}')
print(f'Sum of digits is : {result}')