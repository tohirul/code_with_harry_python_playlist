
# random marks between 70 - 100

marks = [75, 93, 99, 89, 81, 74, 84]


def divide_map(x):
    return x / 2


# marks_list = [divide_map(mark) for mark in marks]
marks_list = list(map(divide_map, marks))
print(marks_list)


# write some documents of users
user_list = [
    {
        "name": "John",
        "age": 23,
        "gender": "male"
    },
    {
        "name": "Jane",
        "age": 25,
        "gender": "female"
    },
    {
        "name": "Jack",
        "age": 27,
        "gender": "male"
    }
]

# for user in user_list:
#     write_messge(user)

list(map(lambda user: print(
    f"Hello {user['name']}, your age is {user['age']}."), user_list))
