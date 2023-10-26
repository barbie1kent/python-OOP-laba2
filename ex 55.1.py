class Text:
    def __init__(self, text):
        self.__text = text

    def count_words(self):
        return len(self.__text.split())

    def reverse(self):
        return self.__text[::-1]

text = Text("hello World 123 123!!!1")
word_count = text.count_words()
reversed = text.reverse()

print("Word count:", word_count)
print("Reversed text:", reversed)
