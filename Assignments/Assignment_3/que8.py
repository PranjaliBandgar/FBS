#8.Write a program to prompt user to enter userid and password. 
# After verifying userid and password display a 4 digit random number 
# and ask user to enter the same. If user enters the same number then 
# show him success message otherwise failed. (Something like captcha)

import random

user_ID = input('Enter username:')
password = input('Enter password:')

if(user_ID == 'abc' and password == 1234):
    num = random.randint(1000,9999)
    print('Enter 4 digit number :',num)
    user_num = int(input())

    if(num == user_num):
        print('Login successfully.')
else:
    print('Login Failed')