# 7.Find the sum of three-digit number.

# Taking inputs from user 
num = int(input('Enter three digit number:'))

first_digit = num // 100 # Gets the hundreds place
second_digit = (num // 10) % 10 # Gets the tens place 
third_digit = num % 10 # Gets the units place

sum = first_digit + second_digit + third_digit

print(f'Total sum of three digits are {sum}')