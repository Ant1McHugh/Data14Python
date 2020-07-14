from random import choice
from hangman_words import word_list


class Brain:
    # This class is for setting up the info about the word being used
    def __init__(self):
        # This will let us see the length of the word
        # And the word fully written out
        self.choose_word = choice(word_list)
        self.word_length()

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


class Game:
    # This will set out the rules of the game
    def __init__(self):
        self.brain = Brain()
        self.lives = 10  # Once you hit 0 lives you will lose
        self.view = []
        print(self.brain.choose_word)
        self.game_board()
        self.guess()

    def game_board(self):
        board = "_" * self.brain.word_length()
        for underscore in board:
            self.view.append(underscore)
        print("Welcome to Hangman! This is your word.")
        print(self.view)

    def guess(self):
        # This section lets you guess a letter

        guessing_list = []

        correct_guess_list = []

        correct_guess_count = 0

        guessing = input("Please guess a letter.\n").upper()

        guessing_list.append(guessing)

        while self.lives != 0:

            while guessing.isnumeric():
                # This ensures the input is not a number
                print("That is not a single letter, please try again")
                guessing = input("Please guess a letter.\n").upper()
                guessing_list.append(guessing)

            while not guessing.isnumeric():
                # This ensures you only input 1 letter  at a time
                if len(guessing) != 1:
                    print("That is not a single letter, please try again.")
                    guessing = input("Please guess a letter.\n").upper()
                    guessing_list.append(guessing)

                elif guessing.upper() in self.brain.choose_word:
                    # This is the result of a correct guess
                    # if guessing.upper() not in correct_guess_list:
                    guess_check = self.brain.letter_check(guessing)
                    for letter_index in guess_check:
                        self.view[letter_index] = guessing.upper()
                    print(self.view)
                    if guessing not in correct_guess_list:
                        correct_guess_count += 1
                        correct_guess_list.append(guessing)
                        if "_" in self.view:
                            print("Good guess! Keep it going.")
                            guessing = input("Please guess a letter.\n").upper()
                            guessing_list.append(guessing)
                        else:
                            print("Congratulations! You have won!")
                            break

                    elif guessing in correct_guess_list:
                        print("You have already guessed that letter! Try again.")
                        guessing = input("Please guess a letter.\n")
                        guessing_list.append(guessing)


                    elif guessing.upper() not in self.brain.choose_word:
                        # This is the result of an incorrect guess
                        self.lives -= 1
                        if self.lives != 0:
                            print(f"Unlucky! You have {self.lives} lives remaining.")
                            guessing = input("Please guess a letter.\n")
                            guessing_list.append(guessing)
                        else:
                            break

        if self.lives == 0:
            return "You are out of lives. Game Over!"


hangman = Game()
