import datetime


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, salary)

    @staticmethod
    def is_workday(day):
        return day.weekday() not in [5, 6]


emp_str = 'John-100000'
employee = Employee.from_string(emp_str)
print(f"Employee Details: \n Name: {employee.name}\n Salary: {employee.salary}")


my_date = datetime.date(2024, 12, 17)
# print(Employee.is_workday(my_date))
