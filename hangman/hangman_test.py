from random import choice
from hangman_words import word_list

class Brain:
    # This class is for setting up the info about the word being used
    def __init__(self):
        # This will let us see the length of the word
        # And the word fully written out
        self.choose_word = choice(word_list)
        self.word_length()
        print(self.choose_word)

    def word_length(self):
        self.length = len(self.choose_word)
        return self.length

    def letter_check(self, guess):
        letter_index = []
        counter = 0
        for letter in self.choose_word:
            if guess.upper() == letter:
                letter_index.append(counter)
            counter += 1
        return letter_index

hangman = Brain()
print(hangman.letter_check("r"))