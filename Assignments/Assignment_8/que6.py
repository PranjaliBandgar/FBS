#Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def fibonacci_series(n):
    if n <= 0:
        return 0 
    elif n == 1:
        return [1]

    series = [1,1]
    for _ in range(2,n):
        series.append(series[-1] + series[-2])
    return series

num = int(input('Enter the value of n:'))
fib_series = fibonacci_series(num)
print(f'Fibonacci series : {fib_series}')