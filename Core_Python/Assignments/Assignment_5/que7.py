#7.Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
import math 
def factorial(n):
    return sum(math.factorial(i) for i in range(1,n + 1))

n = 9
print('Sum of factorial : ',factorial(n))

#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
def exponent(n):
    return sum(n ** i for i in range(1,n + 1))

n = 7
print('Sum of exponent : ',exponent(n))


#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# (1+2+4+8+.....+2^n-1)
def geometric_series(n):
    sum = 2^n-1
    return (2 ** n) - 1

n = 5
print('Sum of geometric series : ',geometric_series(n))

#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
def power_divsion(n):
    return sum((n ** i)/i for i in range(1,11))

n = 2
print('Sum of series : ',power_divsion(n))

#e. x - x2/3 + x3/5 - x4/7 + .... to n terms

def series(x,n):
    total = 0
    for i in range(1,n+1):
        denominator = 2 * i -1
        term = (x ** i) / denominator

        # Add odd terms ,subtract even terms
        if i % 2 != 0:
            total += term
        else:
            total -= term
    return total

x,n =2,4
print('Sum of series : ',series(x,n))