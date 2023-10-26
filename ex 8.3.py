class Student:
    name = None
    surname = None

    def twoFirstLetters(self):
        print(self.name[0].upper(), end='')
        print(self.surname[0].upper(), end='')

student = Student()

student.name = 'gosha'
student.surname = 'vasilkov'

student.twoFirstLetters()