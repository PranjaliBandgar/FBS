#9.Input 5 subject marks from user and display grade
#  (eg.First class,Second class ..)

sub1 = float(input('Enter the marks of first subject:'))
sub2 = float(input('Enter the marks of second subject:'))
sub3 = float(input('Enter the marks of third subject:'))
sub4 = float(input('Enter the marks of fourth subject:'))
sub5 = float(input('Enter the marks of fifth subject:'))

sum = sub1 + sub2 + sub3 + sub4 + sub5
avg = sum / 5

if(avg >= 90):
    print('Grade: First class')

elif(avg >= 80):
    print('Grade: Second Class')

elif(avg >=70):
    print('Grade: Third class')
else:
    print(f'Avarage student.')