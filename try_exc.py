def check_number(num):
    if num == 0:
        raise ValueError("You entered zero")
    elif num < 0:
        raise ValueError("You entered a negative number")
    else:
        return num


def get_number():
    while True:
        num = input("Enter a positive number: ")
        try:
            num = int(num)
            check_number(num)  # Check the number after converting to int
            return num
        except (ValueError, IndexError, TypeError) as e:
            print(f"Error: {e}. Please try again.")


num = get_number()

print(f'You entered {num}')

# print multiplication table for the number
print("Multiplication table:")

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
