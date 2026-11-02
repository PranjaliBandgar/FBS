# 5. Write a program to enter P, T, R and calculate Compound Interest.

#Taking inputs from user
P = float(input('Enter the priciple ammount (P):'))
T = float(input('Enter the time (T):'))
R = float(input('Enter the rate (R):'))

# calculate compound interest using P,R,T formula
CI = (P * ((1+R/100) ** T )) - P

# print the compound interest
print(f'Compound Interest is {CI} ')