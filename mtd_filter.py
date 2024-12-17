# write a list of students of a school with proper details

student_list = [
    {
        "name": "John",
        "age": 23,
        "gender": "male",
        "class": "10th"
    },
    {
        "name": "Jane",
        "age": 25,
        "gender": "female",
        "class": "11th"
    },
    {
        "name": "Jack",
        "age": 27,
        "gender": "male",
        "class": "12th"
    },
    {
        "name": "Jill",
        "age": 29,
        "gender": "female",
        "class": "13th"
    },
    {
        "name": "Joe",
        "age": 31,
        "gender": "male",
        "class": "14th"
    }
]


def senior_student(student):
    return student["age"] >= 26


senior_student_list = list(filter(lambda st: st["age"] >= 26, student_list))
print("Senior Students:", senior_student_list)
