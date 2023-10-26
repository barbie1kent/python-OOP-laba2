class Employee:
    def __init__(self, name: str, salary: int, age: int):
        self.__name = name
        self.__salary = salary
        self.__age = age

employee = Employee('Gosha', 1000000, 49)