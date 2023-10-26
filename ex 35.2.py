class User:
    __name = None
    __surname = None

  def setName(self, name):
    self.__name = name

  def getName(self):
    return self.__name

  def setSurname(surname):
    self.__surname = surname

  def getSurname(self):
    return self.__surname

class Employee(User):
  def getFull(self):
	return self.__name + ' ' + self.__surname

employee = Employee()

employee.setName("John")

name = employee.getName()
print("Name:", name)

employee.setSurname("Doe")

surname = employee.getSurname()
print("Surname:", surname)

