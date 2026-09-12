#3.3. Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
import math
def sum_of_series(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total
n = int(input('Enter the value of n:'))
result = sum_of_series(n)
print(f'The sum of serires from 1 to {n} is:{result}')
#b. 1!+ 2! + 3! + 4!+..... + n!

def factorial(n):
    fac_sum = 0
    for i in range(1,n + 1):
        fac_sum+= math.factorial(i)
    return fac_sum

num = int(input('Enter the value of n:'))

result = factorial(num)
print(f'The sum of the series is : {result}')

#c. 1^1 + 2^2 + 3^3+ ...... n^n

def power_sum(n):
    power_sum = 0
    for i in range(1,n + 1):
        power_sum+= i ** i
    return power_sum

num = int(input('Enter the value of n:'))

result =power_sum(num)
print(f'The sum of the series is : {result}')