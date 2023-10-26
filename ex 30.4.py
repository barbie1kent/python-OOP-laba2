class User:
  def setName(self, name, salary, surname):
    self.name = name
    self.salary = salary
    self.surname = surname

  def getName(self):
    return self.name

  def getSalary(self):
    return self.salary

  def getSurname(self):
    return self.surname

class Employee(User):
    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSurname(self, surname):
        self.surname = surname

    def getSurname(self):
        return self.surname

employee = Employee()

employee.setName('Gosha')

name = employee.getName()
print(name)