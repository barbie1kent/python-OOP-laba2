class Employee:
    name = None
    salary = None

    def show(self):
        print(self.name)

employee = Employee()

employee.name = 'Gosha'


employee.show()