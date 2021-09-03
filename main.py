student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {}

for score in student_scores:
    score_value = student_scores[score]
    if score_value >= 91 and score_value <= 100:
        student_grades[score] = "Outstanding"
    elif score_value >= 81 and score_value <= 90:
        student_grades[score] = "Exceeds Expectations"
    elif score_value >= 71 and score_value <= 80:
        student_grades[score] = "Acceptable"
    elif score_value <= 70:
        student_grades[score] = "Fail"

print(student_grades)