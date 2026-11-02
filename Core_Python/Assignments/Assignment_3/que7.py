#4.Write a program to check if user has entered correct 
#  userid and password.

correct_id = 'Pranjali'
correct_password = 12345

userID = input('Enter user ID:')
password = input('Enter password:')

if (correct_id == userID) and (correct_password == password):
    print(f'Login successfuly.')
else:
    print(f'Please enter valid user id and password.')
