# 8.Write a program to convert days into years, weeks and days.

#Taking inputs from user
Days = int(input('Enter days :'))

# first calculate years and print
Years = Days // 365
print(f'The total years are {Years}')

# after calculating years new days calculate and print
NewDays = Days % 365
print(f'New days are {NewDays}')

# calculate weeks  and print
Weeks = NewDays // 7
print(f'The total weeks are {Weeks}')

# calculate remaining days and print
RemainingDays = NewDays % 7
print(f'Remaining days are {RemainingDays}')