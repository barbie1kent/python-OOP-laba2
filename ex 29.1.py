class User:
  def setName(self,name):
    self.name = name

  def getName(self):
    return self.name

class Employee(User):
    pass
employee = Employee()

employee.setName('Gosha')

name = employee.getName()
print(name)