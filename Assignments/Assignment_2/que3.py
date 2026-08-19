# 3.Convert distant given in feet and inches into meter and centimeter.

# taling inputs from user
feet = int(input('Enter feet:'))
inches = int(input('Enter inches:'))

# calculate meter and centimeter 
# multiply the feet by 30.48 and inches by 2.54 to get total 
# centimeters, then divide by 100 to get meters.
centimeter = (feet * 30.48) + (inches * 2.54)
meter = centimeter / 100

# print the output
print(f'Feet and Inches are in centimeter is {centimeter}')
print(f'Feet and inches are in meter is {meter:.2f}')

