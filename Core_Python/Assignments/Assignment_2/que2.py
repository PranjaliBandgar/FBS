# 2.Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# Taking inputs from user 
celsius = float(input('Enter the temperature in Celsius:'))

# calculate Fahrenheit  (C/5 = (F-32)/9) i.e F = (c*9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

# print output
print(f'{celsius}°C to {fahrenheit}°F ')