#13.Write a program to input electricity unit charges and calculate 
# total electricity bill according to the given condition:
#   For first 50 units Rs. 0.50/unit
#   For next 100 units Rs. 0.75/unit
#   For next 100 units Rs. 1.20/unit
#   For unit above 250 Rs. 1.50/unit
#   An additional surcharge of 20% is added to the bill

units = float(input('Enter total units:'))
amount = 0
#   For first 50 units Rs. 0.50/unit
if (units <= 50):
    amount = units * 0.50

#For next 100 units Rs. 0.75/unit
elif(units <= 150): # 50 + 100 = 150 
    amount = (50 * 0.50) + ((units - 50) * 0.75)

#For next 100 units Rs. 1.20/unit 
elif(units <= 250): # 150 + 100 = 250
    amount = (50 * 0.50) + (100 * 0.75 ) + ((units - 150) * 1.20)

#   For unit above 250 Rs. 1.50/unit
else:
    amount = (50 * 0.50) + (100 * 0.75 ) + (100 * 1.20) + ((units -250) * 1.50)

# An additional surcharge of 20% is added to the bill
add_surcharge = amount * 0.20
total_amount = amount + add_surcharge

print(f'Electricity charges: Rs {amount:.2f}')
print(f'Additional surcharge is: {add_surcharge: .2f}')
print(f'Total electricity charges is: {total_amount:.2f}')