class Text:
    def __init__(self, text):
        self.__text = text

    def count_characters_no_spaces(self):
        return len(self.__text.replace(' ', ''))

text = Text("hello World 123 123!!!1")

char_count_no_spaces = text.count_characters_no_spaces()

print("символы без пробелов:", char_count_no_spaces) # символы без пробелов
