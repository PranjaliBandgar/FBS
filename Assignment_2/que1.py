# 1. Convert the time entered in hh,min and sec into seconds.

# Taking inputs from user 
hrs = int(input('Enter hours:'))
min = int(input('Enter minutes:'))
sec = int(input('Enter seconds:'))

# Calculate total seconds according to hrs,min and sec 
total_seconds = (hrs * 3600) + (min * 60) + sec

# print the output
print(f'Total seconds are {total_seconds}')