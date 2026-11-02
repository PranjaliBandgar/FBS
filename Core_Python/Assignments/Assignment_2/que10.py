# 10.Write a program to reverse three-digit number.

num = int(input('Enter three digit number:'))

a = num //100           # hundreds place
b = (num //10) % 10     # tens place
c = num % 10            # ones place

reverse_num = (c * 100) + (b * 10) + a

print(f'Reverse number is {reverse_num}')