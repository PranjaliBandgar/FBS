#9.WAP to print all numbers in a range divisible by a given number.

# logic = iterate through the range and check if each number gives a remainder of 0 when divided by divisor

start = int(input('Enter starting range:'))
end = int(input('Enter ending range:'))
div = int(input('Enter divisor:'))

for i in range(start, end + 1):
    if i % div == 0:
        print(i)