class Text:
    def __init__(self, text):
        self.__text = text

    def count_letters(self):
        letters = [char for char in self.__text if char.isalpha()]
        return len(letters)

text = Text("hello World 123 123!!!1")

letter_count = text.count_letters()

print("буквы:", letter_count) # буквы
