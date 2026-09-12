#4.Sum of all odd numbers between 1 to n

def sum_of_odd(n):
    total_sum = 0
    for i in range(1,n+1):
        if i % 2 != 0 :
            total_sum +=i
    return total_sum

num = int(input('Enter the value of n:'))
result = sum_of_odd(num)
print(f'The sum of odd numbers 1 to {num} is {result}')