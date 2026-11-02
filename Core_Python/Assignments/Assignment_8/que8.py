# 8.Write a program find reverse of a number

def reverse_number(n):
    reverse_number = 0

    while n > 0:
        last_digit = n % 10 # get the last digit
        reverse_number = (reverse_number * 10) + last_digit 
        n = n // 10 # remove last digit

    return reverse_number

num = int(input('Enter number to reverse:'))
original_num = reverse_number(num)
print(f'Original number: {num}')
print(f'Reversed number: {original_num}')