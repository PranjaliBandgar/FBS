#4.WAP to print factorial of a number.
# Factorial = 1 * 2 * 3 * n (logic)
num = int(input('Enter number:'))
fact = 1 # because when we multiply 0 ans will be zero
for i in range(1,num+1):
    fact *= i 
print(f'Factorial:',fact)
