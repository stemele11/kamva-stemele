student_scores={
    'Harry':81,
    'Ron':78,
    'Hermione':99,
    'Draco':74,
    'Neville':62,
}

student_grades={}

for student in student_scores:
    if student_scores[student]>=91 :
        student_grades[student]='Outstanding'
    elif student_scores[student]>=81:
        student_grades[student]='Exceeds Expectation'
    elif student_scores[student]>=71:
        student_grades[student]='Acceptable'
    else:
        student_grades[student]='Fail'

print(student_grades)



