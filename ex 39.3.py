class User:
  def setName(self, name):
    self._name = name

  def getName(self):
    return self._name

class Employee(User):
  def setYear(self, year):
    self._year = year

  def getYear(self):
    return self._year

class Programmer(Employee):
  def setSkill(self, skill):
    self._skill = skill

  def getSkill(self):
    return self._skill

class Designer(Employee):
  def setActivity(self, activity):
    self._activity = activity

  def setActivity(self):
    return self._activity