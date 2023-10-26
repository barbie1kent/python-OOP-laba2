class User:
  def setName(self, name, salary):
    self.name = name
    self.salary = salary

  def getName(self):
    return self.name

  def getSalary(self):
    return self.salary

class Employee(User):
    def setSalary(self, year):
        self.year = year

    def getSalary(self):
        return self.year

    def setSurname(self, year):
        self.surname = surname

    def getSurname(self):
        return self.surname