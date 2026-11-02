# 10.Write a program to check if person is eligible to marry or not
#  (male age >=21 and female age>=18)

gender = input('Enter gender(M/F):')
age = int(input('Enter age :'))

if (gender == 'F'):
    if(age >= 18):
        print(f'Girl is eligible for marriage')
    else:
        print(f'Girls age is below 18, so she is not eligible for marriage.')
else:
    if(age >= 21):
        print(f'Boy is eligible for marriage.')
    else:
        print(f"Boy's age is below 21, so he is not eligible for marriage.")

