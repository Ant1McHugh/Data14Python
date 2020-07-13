from random import choice
from hangman_words import word_list

class Brain:
    # This class is for setting up the info about the word being used
    def __init__(self, word):
        # This will let us see the length of the word
        # And the word fully written out
        self.length = len(word)
        self.full_word = word


class Game:

    def __init__(self, word):
        for letter in word:
            letter = "_"




random_word = choice(word_list)

hangman = Game(random_word)

print(hangman

