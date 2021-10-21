# with open("file1.txt") as file1_numbers:
#     file1_string = file1_numbers.readlines()
#     file1_int = [int(num) for num in file1_string]

# with open("file2.txt") as file2_numbers:
#     file2_string = file2_numbers.readlines()
#     file2_int = [int(num) for num in file2_string]

# result = [num for num in file1_int if num in file2_int]
# print(result)
import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score>= 60}
print(passed_students)