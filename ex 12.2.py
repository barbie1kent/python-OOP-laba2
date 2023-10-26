class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def Name(self):
        print(self.name)

employee = Employee('Gosha', 10000000000)