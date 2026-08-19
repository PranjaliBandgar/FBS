# 8.Write a program to swap two numbers using third variable.

first_num = int(input('Enter first number:'))
second_num = int(input('Enter second number:'))

print(f'Before swapping numbers are {first_num} and {second_num}')

# use temp to store third number to swap
third_num = first_num
first_num = second_num
second_num = third_num

print(f'After swapping numbers are {first_num} and {second_num}')
