#1.Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

correct_userid = 'admin'
correct_password = 'admin123'

attempts = 3

while attempts > 0:
    user_id = input('Enter userid: ')
    password = input('Enter password: ')

    if user_id == correct_userid and password == password:
        print('Login Successful.')
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f'Incorrect credentials. You have {attempts} attempts(s) left.')
        else:
            print('Please enter correct credentials.')