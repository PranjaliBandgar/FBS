# 6. Write a program to print Fibonacci series using recursion.
#def fibonacci(n):
#    if (n <= 1):
#        return n 
#    else:
#        return fibonacci(n-1) +fibonacci(n-2)
#n = int(input('Enter number:'))
#result = fibonacci(n)
#for i in range(n):
#    print(fibonacci(i),end=" ") 

def fibonacci_series(a,b,n):
    if n==0:
        return 
    else:
        c = a + b
        print(c,end=" ")
        fibonacci_series(b,c,n-1)

n = int(input("Enter number:"))
fibonacci_series(1,0,n)
