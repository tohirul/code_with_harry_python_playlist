
def count_average(marks):
    total_marks = sum(marks)
    return total_marks / len(marks)


marks = [90, 25, 67, 45, 80]
averate_marks = count_average(marks)
print("Average marks: ", averate_marks)
