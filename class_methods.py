

class Employee:
    company_name = "Google"

    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}\nDepartment: {self.department}\nCompany: {Employee.company_name}\n"

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


employee = Employee("John", 25, 100000, "IT")
print(employee.get_details())
employee.change_company("Apple")

print(employee.get_details())
