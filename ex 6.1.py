class Employee:
    def work(self, name, salary):
        return name + ' ' + salary

employee = Employee()

print(employee.work('Gosha', '100000000'))