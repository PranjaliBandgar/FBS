#2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

num_students = int(input('Enter number of students :'))
total_percentage_sum = 0

#for students
for i in range(1,num_students + 1):
    print(f' Student {i}')
    marks_sum = 0

# Accept marks for 5 subject
    for j in range(1,6):
        mark = float(input(f'Enter marks for Subject {j}:'))
        marks_sum += mark

    percentage = (marks_sum / 500) * 100
    total_percentage_sum += percentage

    print(f'Percentage for student {i} :{percentage:.2f}%')

# calculate average percentage of all students
if num_students > 0:
    average_percentage = total_percentage_sum / num_students
    print(f'Avergae percentage of all students: {average_percentage:.2f}')
    