#5. WAP to calculate selling price of book based on cost price 
# and discount.

# Taking inputs from user 
cost_price = int(input('Enter the cost price of book:'))
discount = int(input('Enter the discount:'))

discount_amount = (cost_price * discount) /100

selling_price = cost_price - discount_amount

print(f'The selling price of book is {selling_price}')