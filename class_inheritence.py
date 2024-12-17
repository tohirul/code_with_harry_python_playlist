
class Employee:
    def __init__(self, name, id, salary, department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department

    def __str__(self):
        return f" Name: {self.name},\n ID: {self.id},\n Salary: {self.salary},\n Department: {self.department}\n"


class Programmer(Employee):
    def __init__(self, name, id, salary, department, programming_language):
        super().__init__(name, id, salary, department)
        self.programming_language = programming_language

    @property
    def show_language(self):
        return f"Programming Language: {self.programming_language}"


newEmployee = Employee("John", 12345, 100000, "IT")

newProgrammer = Programmer("John", 12345, 100000, "IT", "Python")

print(newEmployee)
print(newProgrammer.show_language)
