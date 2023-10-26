class User:
    def setName(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Employee(User):
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

