#9.Write a program to calculate the m to the power n using recursion.

def power(m,n):
    if m < 0 :
        return 0
    elif n == 0:
        return 1
    else:
        return m * power(m,n-1)

m = int(input("Enter the base:"))
n = int(input("Enter the power: "))
result = power(m,n)
print(f"{m} ** {n} = {result}")
