class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def Name(self):
        print(self.name)

    def Salary(self):
        print(self.salary)

    def persentSalary(self):
        print(f'salary: {self.salary * 1.1}')

employee = Employee('Gosha', 100000000)

employee.persentSalary()