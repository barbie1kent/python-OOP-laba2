class User:
  name = None
  position = None
  department = None

  def __init__(self, name, position, department):
    self.name = name
    self.position = position
    self.department = department

  def data(self):
    return data

class Position:
  title = None

  def __init__(self, title):
    self.title = title

class Department:
  name = None

  def __init__(self, name):
    self.name = name