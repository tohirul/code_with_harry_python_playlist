
users = ["John", "Jane", "Jack", "Jill", "Joe"]

# write a for loop that prints the names of the users and uses else
# to print "No users found" if the list is empty


for user in users:
    print(user)
else:
    total_users = len(users)
    if total_users == 0:
        print("No users found")
    else:
        print(f"Total users: {total_users}")
