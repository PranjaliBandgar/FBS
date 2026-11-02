#4. Write a program to find sum of n numbers using recursion.
def sum_of_num(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_num(n-1)
n = int(input("Enter number:"))
res = sum_of_num(n)
print(f"Sum of {n} =",res)