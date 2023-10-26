class User:
  def setName(self, name):
    self.name = name

  def getName(self):
    return self.__capeFirst(self.name)

  def __capeFirst(self, string):
    return string

class Employee(User):
  def setSurname(self, surname):
    self.surname = surname

  def getSurname(self):
    return self.__capeFirst(self.surname)