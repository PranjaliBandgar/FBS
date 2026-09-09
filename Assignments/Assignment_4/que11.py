#11.WAP to check if given number is strong number.

# Logic = A strong number equals the sum of the factorial of its digits (145 = 1! + 4! + 5!)
import math
num = int(input('Enter number:'))

temp = num
total_sum = 0

while temp > 0:
    digit = temp % 10
    total_sum += math.factorial(digit)
    temp //= 10
if total_sum == num:
    print(f'{num} is a strong number.')
else:
    print(f'{num} is not strong number.')
