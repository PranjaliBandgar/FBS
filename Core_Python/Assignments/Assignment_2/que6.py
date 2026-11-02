# 6.WAP to calculate total salary of employee based on basic, 
# da=10% of basic,ta=12% of basic, hra=15% of basic.

basic_salary = float(input('Enter basic salary of employee:'))
da = 0.10 * basic_salary # Dearness Allowance
ta = 0.12 * basic_salary # Travel allowance
hra = 0.15 * basic_salary # House rent allowance

total_salary = basic_salary + da + ta + hra

print(f'Total salary of employee is {total_salary}')
