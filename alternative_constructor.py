import datetime


class Employee:
    company = "Google Inc."

    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, salary)

    @staticmethod
    def is_workday(day):
        return day.weekday() not in {5, 6}  # Use set for efficiency

    def get_employee_details(self):
        return f"Name: {self.name}\nSalary: {self.salary}\nCompany: {self.company}"


# Creating and displaying employee details
emp_str = 'John-100000'
junior_employee = Employee.from_string(emp_str)
print(junior_employee.get_employee_details())

senior_emp_str = "Jason-20000"
senior_employee = Employee.from_string(senior_emp_str)
print(senior_employee.get_employee_details())

# Checking if a date is a workday
my_date = datetime.date(2024, 12, 17)  # Tuesday
print("Is workday:", Employee.is_workday(my_date))
