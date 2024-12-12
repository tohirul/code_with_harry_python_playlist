import random

person_age = int(input("Enter your age: "))

age_diff = 0

while person_age < 18:
    person_age += 1
    age_diff += 1

print(
    "You can vote right now"
    if age_diff == 0
    else f"You will be able to vote in {str(age_diff)} years"
)

print("\n")

random_number = random.randint(1, 10)

user_guess = int(input("Guess the number: "))
guess_count = 0
while user_guess != random_number:
    guess_count += 1
    if guess_count <= 1:
        user_guess = int(input("Wrong ! Guess the number: "))
    else:
        user_guess = int(input("Wrong again ! Guess the number: "))

    if user_guess < random_number:
        print("Too low! Try higher.")
    elif user_guess > random_number:
        print("Too high! Try lower")
    else:
        print("Let's see !!!")

print(f"You guessed it right the random number was {random_number}")
print(f"You guessed it in {str(guess_count)} tries")
