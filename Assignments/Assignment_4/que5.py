#5.WAP to print fibonacci series upto n
# Addition of previous two numbers 

num = int(input('Enter a number:'))
a , b = 0, 1
sum = 0
while a <= num:
    print(a,end = ' ')
    a, b = b, a+b
  

