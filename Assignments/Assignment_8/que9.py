# 9.Write a program to check if entered number is a palindrome or not.

def palindrome_number(num):
    original_number = num
    reversed_number = 0

    while num > 0:
            last_digit = num % 10 # get the last digit
            reversed_number = (reversed_number * 10) + last_digit 
            num = num // 10 # remove last digit
    return original_number == reversed_number
    
num = int(input('Enter number:'))
if palindrome_number(num):
    print(f'{num} is palindrome number.')
else:
    print(f'{num} is not palindrome number.')
