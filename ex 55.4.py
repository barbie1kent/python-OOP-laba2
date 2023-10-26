class Text:
    def __init__(self, text):
        self.__text = text

    def count_spaces(self):
        return self.__text.count(' ')

text = Text("hello World 123 123!!!1")

space_count = text.count_spaces()

print("пробелы:", space_count) # пробелы
