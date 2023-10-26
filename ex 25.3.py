class Employee:
  __name = None

  def __init__(self, name):
    self.__name = name


  def getName(self):
    return self.__name


class EmployeesCollection:

  def __init__(self):
    self.__name = []

  def add(self,employee):
    self.__employees.append(Employee)

  def show(self):
    for Employees in self.__employees:
      print(Employee.getName())

ec = EmployeesCollection

ec.add(Employee('vsevolod'))
ec.add(Employee('lyoha'))
ec.add(Employee('maxim'))

ec.show()