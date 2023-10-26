class Employee:
    name = None
    salary = None

    def show(self):
        print(self.salary)

employee = Employee()

employee.salary = 10000000000


employee.show()