class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name:str, salary:int, age:int):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getAge(self):
        return self.__age


employee = Employee('Gosha', 100000000, 49)