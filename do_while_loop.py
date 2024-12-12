import random

random_number = random.randint(1, 10)
user_guess = int(input("Guess the number: "))
guess_count = 0

# do while loop
while True:
    guess_count += 1
    if user_guess < random_number:
        print("Too low! Try higher.")
    elif user_guess > random_number:
        print("Too high! Try lower")
    else:
        print("You guessed it right")
        break
    user_guess = int(input("Guess the number: "))
print(f"You guessed it in {str(guess_count)} tries")
