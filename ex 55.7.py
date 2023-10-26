class Text:
    def __init__(self, text):
        self.__text = text

    def get_sentence_array(self):
        return self.__text.split('. ')

text = Text("hello World 123 123!!!1")

sentence_array = text.get_sentence_array()

print("массив предложений:", sentence_array) # массив предложений