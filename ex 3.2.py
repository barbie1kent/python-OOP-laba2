class Employee:
    address = None
    age = None
    name = None
    salary = None

    def work(self, employee):
        print(f' address: {employee.address}'
              f' age: {employee.age}'
              f' name: {employee.name}'
              f' salary: {employee.salary}')

employee = Employee()

employee.address = 'street'
employee.age = 20
employee.name = 'Gosha'
employee.salary = 1000000000000

employee.work(employee)