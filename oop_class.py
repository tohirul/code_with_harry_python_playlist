
# write a class for information about a facebook profile information
class Profile:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def profile_dict(self):
        return {"name": self.name, "age": self.age, "gender": self.gender, "occupation": self.occupation}

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nOccupation: {self.occupation}"


# use class profile to create a new profile
myprofile = Profile("John", 23, "male", "student")

print(myprofile.profile_dict())
print(myprofile)

newProfile = Profile("John", 26, "male", "Programmer")
print(newProfile.profile_dict())
print(newProfile)
