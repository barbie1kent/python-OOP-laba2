class Text:
    def __init__(self, text):
        self.__text = text

    def get_word_array(self):
        return self.__text.split()

text = Text("hello World 123 123!!!1")

word_array = text.get_word_array()

print("массив слов:", word_array) # массив слов
