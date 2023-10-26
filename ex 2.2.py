class Employee:
    address = None
    def work(self, employee):
        print(f' address: {employee.address}')

employee = Employee()
employee.address = 'street'

employee.work(employee)