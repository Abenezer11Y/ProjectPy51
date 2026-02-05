class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+ self.meaning + ')'

flash = []
print("Welcome to my Flashcard!")
while(True):
    word = input("Enter a word you want in your flashcard: ")
    meaning = input("Enter a meaning for the word you want in your flashcard: ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0 if you want to add another flashcard but otherwise enter 1: "))

    if(option):
        break

print("Your flashcards")
for i in flash:
    print(">", i)