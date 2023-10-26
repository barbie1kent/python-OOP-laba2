class Student:
    name = None
    surname = None

    def firstLetter(self, str):
        for i in range(len(str)):
            if i != 0:
                print(str[i], end='')
            else:
                print(str[i].upper(), end='')

student = Student()

student.name = 'gosha'
student.surname = 'vasilkov'

student.firstLetter(student.name)