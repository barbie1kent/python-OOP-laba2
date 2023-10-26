class Employee:
    def __init__(self, name:str, salary:str):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.__addSign(self.salary)

    def __addSign(self, num: str):
        return "$" + num

employee = Employee('Gosha', '100000000')

print(employee.getSalary())