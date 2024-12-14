
def get_user_input():
    return input("Please enter a value : ")


def check_operator(operator):
    return operator in ["+", "-", "*", "/", "%", "**", "//"]


def calculate(num_first, num_second, operator):
    output = 0
    match operator:
        case "+":
            output = num_first + num_second
        case "-":
            output = num_first - num_second
        case "*":
            output = num_first * num_second
        case "/":
            output = num_first / num_second
        case "%":
            output = num_first % num_second
        case "**":
            output = num_first ** num_second
        case "//":
            output = num_first // num_second
        case _:
            print("Invalid operator")
            return
    return output


def find_greater(num_first, num_second):
    return max(num_first, num_second)


operator = input("Please enter an operator : ")

while not check_operator(operator):
    print("Invalid operator")
    operator = input("Please enter an operator : ")

first_input = get_user_input()
second_input = get_user_input()

print("The greater number is: ",
      find_greater(int(first_input), int(second_input)))

print("The result is: ",
      calculate(int(first_input), int(second_input), operator))
