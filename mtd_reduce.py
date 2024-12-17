from functools import reduce

# list of marks between 60-100
student_marks = [86, 100, 73, 92, 85, 79, 71, 99]

total_marks = reduce(lambda x, y: x + y, student_marks)

print(total_marks)
