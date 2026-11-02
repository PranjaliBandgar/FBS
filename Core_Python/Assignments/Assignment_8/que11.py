# 11.WAP to check if a given number is Armstrong number or not. For
 #each task create separate functions. 

def count_digits(num):
    # calculate the total number of digits in the given number
    return len(str(num))

def power_sum(num,power):
    # computes the sum of each digit raised to the given power.
    total_sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total_sum += digit ** power
        temp //= 10
    return total_sum

def armstrong(num):
    if num < 0:
        return False
    num_digits = count_digits(num)
    powers_sum = power_sum(num, num_digits)

    return powers_sum == num

num = int(input('Enter a number.'))

if armstrong(num):
    print(f'{num} is an Armstrong number.')

else:
    print(f'{num} is not an Armstrong number.')