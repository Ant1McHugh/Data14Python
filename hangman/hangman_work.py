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
    # This will set out the rules of the game
    def __init__(self, word):
        self.word_length = len(word)
        self.full_word = word
        self.lives = 10  # Once you hit 0 lives you will lose
        self.answer = []
        self.view = []
        for letter in self.full_word:
            self.answer.append(letter)
        for underscore in range(0, len(self.answer)):
            self.view.append("_")
        print("Welcome to Hangman! This is your word.")
        print(self.view)

    def guess(self):
        # This section lets you guess a letter

        guessing_list = []

        guessing = input("Please guess a letter.\n")

        guessing_list.append(guessing)

        while guessing.isnumeric():
            # This ensures the input is not a number
            print("That is not a single letter, please try again")
            guessing = input("Please guess a letter.\n")

        while not guessing.isnumeric():
            # This ensures you only input 1 letter  at a time
            if len(guessing) != 1:
                print("That is not a single letter, please try again.")
                guessing = input("Please guess a letter.\n")
            elif guessing.upper() in self.full_word:
                # This is the result of a correct guess
                index_of_letter = 0
                for letter in self.full_word:
                    if letter == guessing:
                        self.view[index_of_letter] = guessing
                        index_of_letter += 1
                        print("That is correct!")
                    return self.view

            else:
                # This is the result of an incorrect guess
                self.lives -= 1
                return "Unlucky! That is not in the word."


random_word = choice(word_list)

print(random_word)

hangman = Game(random_word)
print(hangman.guess())
