student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

def get_grade(score):
    if score > 91:
        return "Outstanding"
    elif score > 81:
        return "Exceeds Expectations"
    elif score > 71:
        return "Acceptable"
    else:
        return "Fail"

for key in student_scores:
    student_grades[key] = get_grade(student_scores[key])

# 🚨 Don't change the code below 👇
for key in student_grades:
    print(f"{key}: {student_grades[key]}")
