class Validator:

    def __init__(self, str: str):
        self.string = str


    def isNumber(self):
        if self.string.isdigit():
            print('Все символы - числа')
        else:
            print('Не все символы числа')

validator = Validator('8764534567')

validator.isNumber()