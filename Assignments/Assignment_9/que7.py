#6. Write a program to find sum of digits using recursion.
def sum_of_digit(n,sum):
    if (n == 0):
        return sum
    else:
        sum = sum +(n%10)
        n = n // 10
        return sum_of_digit(n,sum)
n = int(input("Enter number:"))
sum = 0
result = sum_of_digit(n,sum)
print(f"Sum of {n} is",result)