# 5. Sum of all prime numbers between 1 to n

def sum_of_prime(num):
    sum = 0
    for i in range(2,num + 1):
        for j in range(2, i):
            if (i % j ==0):
                break
        else:
            print(i)
            sum = sum + i
    return sum

num = int(input('Enter the value of n:'))
result = sum_of_prime(num)
print(f'Sum of prime numbers 1 to {num} is {result}')