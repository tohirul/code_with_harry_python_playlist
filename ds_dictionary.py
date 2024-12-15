
user_info = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_married": False
}

print(user_info["name"])
print(user_info["age"])
print(user_info["city"])

# add new key-value pair
print(user_info.get("is_married"))
print(user_info.get("email"))

print(user_info.items())

for key in user_info:
    print(f'Value of {key}', user_info[key])


# update .values()
additional_info = {
    "email": "john@example.com",
    "phone": "123-456-7890",
    "is_employed": True
}

user_info |= additional_info
print(user_info)


# user_info.clear() will clear the dictionary
# user_info.clear()


# del keyword can also be used to delete a key-value pair
# del user_info["name"]

# pop() method can also be used to delete a key-value pair
# user_info.pop("age")


print(user_info)
