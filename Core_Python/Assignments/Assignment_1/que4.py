# 4.Write a program to enter P, T, R and calculate simple Interest.

#Taking inputs from user
P = int(input('Enter principle amount:'))
T = int(input('Enter the time:'))
R = float(input('Enter the rate:'))

# calculate simple interest using P,R,T formula 
SI = P * T * R /100

# print the simple interest
print(f'Simple intrest is {SI}')