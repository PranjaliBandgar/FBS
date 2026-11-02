# 1.Write a program to calculate the percentage of student based on 
# marks of any 5 subjects.

# Taking inputs from user
sub1 = int(input('Enter the marks of sub1 :'))
sub2 = int(input('Enter the marks of sub2 :'))
sub3 = int(input('Enter the marks of sub3 :'))
sub4 = int(input('Enter the marks of sub4 :'))
sub5 = int(input('Enter the marks of sub5 :'))

# calculate percentage
sum = sub1 + sub2 + sub3 + sub4 + sub5
Percentage = sum/5

# print the percentage 
print(f'Percentage is {Percentage}')
