#3.Write a program to reverse a given number using recursive function.

def reverse(n,rev):
    if n == 0:
        return rev
    else:
        rev = rev * 10 + (n % 10)
        return reverse(n//10,rev)
n = int(input("Enter number:"))
rev = 0
print(f"Reverse of {n} is",reverse(n,rev))
