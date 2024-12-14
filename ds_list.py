
student_list = [
    {
        "name": "John",
        "age": 20,
        "courses": ["Math", "Science", "English"],
        "marks":  [60, 80, 70]
    },
    {
        "name": "Mary",
        "age": 21,
        "courses": ["Math", "Science", "English"],
        "marks":  [90, 80, 70]
    },
    {
        "name": "Peter",
        "age": 22,
        "courses": ["Math", "Science", "English"],
        "marks": [90, 80, 60]
    },
    {
        "name": "Susan",
        "age": 20,
        "courses": ["Math", "Science", "English"],
        "marks": [70, 80, 90]
    },
    {
        "name": "David",
        "age": 21,
        "courses": ["Math", "Science", "English"],
        "marks": [70, 80, 65]
    },
]


def count_average(marks):
    total_marks = sum(marks)
    return total_marks / len(marks)


def student_names(students):
    return [student["name"] for student in students]


print("Student names: ", student_names(student_list))


def student_results(student):
    print("Name: ", student["name"])
    print("Age: ", student["age"])
    print("Courses: ", student["courses"])
    for course in student["courses"]:
        print("Course: ", course)
        print("Marks: ", student["marks"][student["courses"].index(course)])


print("\nStudent Results:")
for student in student_list:
    student_results(student)
    print("\n")
