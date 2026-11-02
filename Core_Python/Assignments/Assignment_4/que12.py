#12. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

# Armstrong number = An armstrong number is a number equal to the sum of its digits each
#  raised to the power of the total number of digits

num = int(input('Enter a number:'))
num_str = str(num)
num_digits = len(num_str)

total_sum = sum(int(digit) ** num_digits for digit in num_str)
if total_sum == num:
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number.')