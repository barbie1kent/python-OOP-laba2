class Employee:
    def __init__(self, name: str, salary: int, age: int):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def Data(self):
        print(f"name: {employee.__name}"
              f"\nsalary: {employee.__salary}"
              f"\nage: {employee.__age}")

employee = Employee('Gosha', 100000, 49)

employee.Data()