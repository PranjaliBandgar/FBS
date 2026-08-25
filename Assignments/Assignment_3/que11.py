#11.Accept age of five people and also per person ticket amount and 
# then calculate total amount to ticket to travel for all of them 
# based on following condition :
    #a. Children below 12 = 30% discount
    #b. Senior citizen (above 59) = 50% discount
    #c. Others need to pay full.

ticket_price = float(input('Enter ticket price per person:'))

# Five person age from user
age1= int(input('Enter age of person1:'))
age2= int(input('Enter age of person2:'))
age3= int(input('Enter age of person3:'))
age4= int(input('Enter age of person4:'))
age5= int(input('Enter age of person5:'))

# calculate cost for person 1
if(age1 < 12):
    cost1 = ticket_price * 30/100
elif(age1 < 59):
    cost1 = ticket_price * 50/100
else:
    cost1 = ticket_price

# calculate cost for person 2
if(age2 < 12):
    cost2 = ticket_price * 0.70
elif(age2 < 59):
    cost2 = ticket_price * 0.50
else:
    cost2 = ticket_price

# calculate cost for person 3
if(age3 < 12):
    cost3 = ticket_price * 30/100
elif(age3 < 59):
    cost3 = ticket_price * 50/100
else:
    cost3 = ticket_price

# calculate cost for person 4
if(age4 < 12):
    cost4 = ticket_price * 30/100
elif(age4 < 59):
    cost4 = ticket_price * 50/100
else:
    cost4 = ticket_price

# calculate cost for person 5
if(age5 < 12):
    cost5 = ticket_price * 30/100
elif(age5 < 59):
    cost5 = ticket_price * 50/100
else:
    cost5 = ticket_price

# Total cost for 5 person
total_cost = cost1 + cost2 + cost3 + cost4 + cost5

# Display total amount for 5 person
print(f'The total amount for 5 person is Rs {total_cost}')