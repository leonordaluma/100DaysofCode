student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for n in student_scores:
    current_number = n
    if current_number > max_score:
        max_score = current_number
    else:
        temp = current_number

print(f"The highest score is: {max_score}")