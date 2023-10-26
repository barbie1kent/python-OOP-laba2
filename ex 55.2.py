class Text:
    def __init__(self, text):
        self.__text = text

    def count_characters(self):
        return len(self.__text)

text = Text("hello World 123 123!!!1")

char_count = text.count_characters()


print("символы:", char_count) # символы
