#6.WAP to check if a given number is prime or not 
# Prime number = number is divisible by 1 or itself

num = int(input('Enter a number:'))

if num <= 1:
    print(f'Not prime.')

else:
    for i in range(2,num):
        if num % i == 0:
            print(f'Not prime number.')
            break
    else:
        print(f'Number is prime number.')
