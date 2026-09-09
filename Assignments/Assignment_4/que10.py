#10.WAP to check if given number is Perfect number.

# Logic = A perfect number equals the sum of its proper divisors(6 = 1+2+3)

num = int(input('Enter number:'))
sum_divisor = 0

for i in range(1,num):
    if num % i == 0:
        sum_divisor += i
if sum_divisor == num:
    print(f'Number is perfect number.')
else:
    print(f'Not perfect number.')