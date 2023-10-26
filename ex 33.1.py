class User:
  def __init__(self, name, surname):
        self.name = name
        self.surname = surname

  def getName(self):
    return self.name

class Employee(User):
  def __init__(self,name, surname, year):
		super(name, surname)
		self.year = year

  def getYear(self):
    return self.year

