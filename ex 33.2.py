class User:
  def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

  def getName(self):
    return self.name

  def getSalary(self):
    return self.Salary

  def getAge(self):
      return self.age

class Employee(User):
    def __init__(self, name, salary, age):
        super().__init__(name, salary, age)
