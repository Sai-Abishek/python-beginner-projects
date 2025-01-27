student_score = {
    "Vinay":100,
    "Nirmal":80,
    "Ganesh":96,
    "Abisheek":100,
    "Jaishankar":70
}

student_grades = {}

for key,value in student_score.items():
    if value >= 91 and value <= 100:
        student_grades[key] = "Outstanding"
    elif value >= 81 and value <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif value >= 71 and value <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
        
print(student_grades)