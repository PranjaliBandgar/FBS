# 11.Write a program to accept an integer amount from user and 
# tell minimum number of notes needed for representing that amount.

amount = int(input('Enter amount:'))

# 2000 notes
notes_of_2000 = amount // 2000
print(f'Total {notes_of_2000} notes of 2000')

new_amount_1 = amount % 2000
print(f'First new amount {new_amount_1}')

print('************************************')

# 500 notes
notes_of_500 = new_amount_1 // 500
print(f'Total {notes_of_500} note of 500')

new_amount_2 = new_amount_1 % 500
print(f'Second new amount is {new_amount_2}')

print('************************************')

# 200 notes
notes_of_200 = new_amount_2 // 200 
print(f'Total {notes_of_200} notes of 200')

new_amount_3 = new_amount_2 % 200
print(f'Third new amount is {new_amount_3}')

print('************************************')

# 100 notes
notes_of_100 = new_amount_3 // 100 
print(f'Total {notes_of_100} notes of 100')

new_amount_4 = new_amount_3 % 100
print(f'Fourth new amount is {new_amount_4}')

print('************************************')

# 50 notes
notes_of_50 = new_amount_4 // 50 
print(f'Total {notes_of_50} notes of 50')

new_amount_5 = new_amount_4 % 50
print(f'Fifth new amount is {new_amount_5}')

print('************************************')

# 20 notes
notes_of_20 = new_amount_5 // 20 
print(f'Total {notes_of_20} notes of 20')

new_amount_6 = new_amount_5 % 20
print(f'Sixth new amount is {new_amount_6}')

print('************************************')

# 10 notes
notes_of_10 = new_amount_6 // 10
print(f'Total {notes_of_10} notes of 10')

new_amount_7 = new_amount_6 % 10

Remaining_amount = new_amount_7
print(f'Remaining new amount is {Remaining_amount}')

print('************************************')
total_notes = notes_of_2000 + notes_of_500 + notes_of_200 + notes_of_100 + notes_of_50+ notes_of_20 + notes_of_10
print(f'There are total number of notes in amount of {amount} is {total_notes}')
