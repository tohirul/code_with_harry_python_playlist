
star_lines = int(input("Enter the number of star lines: "))


# star triangle
for i in range(star_lines):
    space = (" " * (star_lines-i-1))
    stars = ("*" * ((1 + i) + i if i >= 1 else 1))
    print(space + stars)

print("\n")

for i in range(star_lines):
    print("*" * (i+(1 if i == 0 else i)))

print("\n")

for i in range(star_lines):

    print("*" * (star_lines - i + 1 if i == 0 else star_lines - i))

print("\n")

for i in range(star_lines):

    print(" " * (star_lines - i - 1) + "*" * (i + 1 if i == 0 else i + 1))
