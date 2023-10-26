class Employee:
  __name = None

  def __init__(self, name, salary):
    self.__name = name
    self.__salary = salary

  def getName(self):
    return self.__name

  def getSalary(self):
    return self.__salary

class EmployeesCollection:
	__employees = None

employees = [
    Employee('vasya', 1000),
	Employee('petya', 2000),
	Employee('volodya', 3000)
]