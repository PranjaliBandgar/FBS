# 4. WAP to print Armstrong number within a given range

low = int(input('Enter lowest range:'))
heigh = int(input('Enter heighest range:'))

print(f'Armstrong numbers between {low} and {heigh}:')

for num in range(low,heigh+1):
    num_str = str(num)
    power = len(num_str)

    total_sum = sum(int(digit) ** power for digit in num_str)

    if num == total_sum:
        print(num)
print()