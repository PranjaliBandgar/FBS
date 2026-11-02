#1.Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!
#Note : For fact and sum two recursive functions

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

def sum_factorial(n):
    if n <=1:
        return 1
    return factorial(n) + factorial(n-1)
n = int(input('Enter number:'))
total_sum = sum_factorial(n)
print(f'Sum of factorial is {total_sum}')







