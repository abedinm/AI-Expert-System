# Problem 5 - Student Directory (Dictionaries)
# A dictionary where keys are student IDs and values hold name, age and grade,
# with functions to add and query records.

student_db = {
    "S101": {"name": "Alice", "age": 20, "grade": "A"},
    "S102": {"name": "Bob", "age": 21, "grade": "B"},
}


def add_student(db, student_id, name, age, grade):
    # assigning to a key adds it if new, or updates it if it already exists
    db[student_id] = {"name": name, "age": age, "grade": grade}


def get_student(db, student_id):
    if student_id in db:
        return db[student_id]
    return None


def students_with_grade(db, grade):
    names = []
    for info in db.values():
        if info["grade"] == grade:
            names.append(info["name"])
    return names


add_student(student_db, "S103", "Charlie", 22, "A")
add_student(student_db, "S102", "Bob", 21, "A+")   # update an existing record

print("All students:")
for sid, info in student_db.items():
    print(" ", sid, info)

print("Query S101:", get_student(student_db, "S101"))
print("Query S999:", get_student(student_db, "S999"))
print("Grade A students:", students_with_grade(student_db, "A"))
