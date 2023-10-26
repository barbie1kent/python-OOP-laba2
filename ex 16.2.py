class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name:str, salary:str, age:int):
        self.__name = name
        self.__salary = salary
        self.__age = age

employee = Employee('Gosha', 100000000, 49)