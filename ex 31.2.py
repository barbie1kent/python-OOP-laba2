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
        if age >= 18 and age <= 65:
            self.age = age
        else:
            raise Exception("employee age error")

    def getAge(self):
        return self.age


employee = Employee()
employee.setAge(56)

print(employee.getAge())