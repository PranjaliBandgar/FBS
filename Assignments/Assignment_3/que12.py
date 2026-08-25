#12.Write a program to check if given 3 digit number is a palindrome 
# or not.

num = int(input('Enter 3 digit number.'))

first_digit = num // 100
last_digit = num % 10

if (first_digit == last_digit):
    print(f'{num} is palindrome number.')
else:
    print(f'{num} is not palindrome number.')