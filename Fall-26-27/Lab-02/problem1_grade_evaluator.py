# Problem 1 - Grade Evaluator (Lists & Conditionals)
# Use if-elif-else inside a loop to evaluate each score (0-100) and store the grades in a list.

scores = [85, 92, 78, 60, 45, 95]
grades = []

for score in scores:
    if score < 0 or score > 100:
        grade = "Invalid"
    elif score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    grades.append(grade)

print(grades)

for score, grade in zip(scores, grades):
    print(score, "->", grade)
