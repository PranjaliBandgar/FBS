#8. Write a program to check whether a number is prime or not using recursion.
def is_prime(n,number):
    if n <=1:
        return False
    elif number == n:
        return True
    elif n % number == 0:
        return False
    return is_prime(n,number+1)

n = int(input('Enter number:'))
result = is_prime(n,2)
if result:
    print(f'{n} is prime number.')
else:
    print(f'{n} is not prime number.')