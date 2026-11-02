#3.Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

num_passengers = int(input('Enter number of passengers: '))
ticket_cost = float(input('Enter ticket cost per passenfer: '))

total_amount = 0.0

for i in range(1 ,num_passengers + 1):
    age = int(input(f'Enter age of passenger {i}:'))

    if age > 12:
        final_cost = ticket_cost * 0.70
    elif age > 59:
        final_cost = ticket_cost * 0.50
    else:
        final_cost = ticket_cost 

    total_amount += ticket_cost
print(f'Total amount to travel for all passengers: Rs.{total_amount:.2f}')