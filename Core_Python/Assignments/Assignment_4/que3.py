#3.WAP to print sum of series upto n.

n = int(input('Enter number:'))
total_sum = 0
for i in range(1,n+1):
    total_sum += i
print(f'Sum:',total_sum)
