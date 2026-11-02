#2.Write a program to check if given number is Armstrong or not using recursive
#function.
def sum_of_power(num,power):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** power) + sum_of_power(num // 10,power)

def is_armStrong(num):
    power = len(str(num))
    return num == sum_of_power(num,power)

number = int(input('Enter a number:'))
if is_armStrong(number):
    print(f'{number} is Armstrong number.')
else:
    print(f'{number} is not Armstrong number.')
