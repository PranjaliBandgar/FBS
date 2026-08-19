# 9.Write a program to swap two numbers without using third variable.

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

print(f'Before swaping numbers are {num1} and {num2}')

num1 = num1 + num2 
num2 = num1 - num2
num1 = num1 - num2

print(f'After swaping numbers are {num1} and {num2}')