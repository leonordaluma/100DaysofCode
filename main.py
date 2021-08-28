student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

number_of_heights = 0
sum_of_heights = 0
for n in student_heights:
    number_of_heights += 1
    sum_of_heights += n

average_height = round(sum_of_heights / number_of_heights)
print(average_height)
