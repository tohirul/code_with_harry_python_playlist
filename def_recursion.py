
def num_factorial(num):
    return 1 if num in (0, 1) else num * num_factorial(num - 1)


numb = int(input("Enter a number to find factorial: "))
print("Factorial of ", numb, " is ", num_factorial(numb))

print("\n")


def find_fibonacci():
    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

    numb = int(input("Enter a number to find fibonacci: "))
    print("Fibonacci of ", numb, " is ", fibonacci(numb))


find_fibonacci()
