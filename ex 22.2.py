class Validator:
    def __init__(self, str: str):
        self.string = str

    def isEmail(self):
        if (self.string.find('@') != -1):
            print('корректный email')
        else:
            print('некорректный email')


validator = Validator('bububu:gmail.com')

validator.isEmail()