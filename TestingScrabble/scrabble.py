import random
# Used to get random letters for the hand

class ScrabbleGame:

    def __init__(self):
        # This sets the letters that can be picked out for the hand later on
        self.alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        # These dictionaries set what letters go in each points category
        self.one_point_letters = {"l", "s", "u", "n", "r", "t", "o", "a", "i", "e"}
        self.two_point_letters = {"g", "d"}
        self.three_point_letters = {"b", "c", "m", "p"}
        self.four_point_letters = {"f", "h", "v", "w", "y"}
        self.five_point_letters = {"k"}
        self.eight_point_letters = {"j", "x"}
        self.ten_point_letters = {"q", "z"}
        self.hand = 0 # This regulates the hand size at the start of the game
        self.tiles_in_hand = []
        self.chosen_word = " "
        self.start_round()
        self.hand_size()
        self.choose_word()
        self.word_score()
        self.next_round()

    def letter_score(self, word):
        # This method finds the score of individual letters in a word
        for letter in word:
            if letter in self.one_point_letters:
                score = 1
                return score
            elif letter in self.two_point_letters:
                score = 2
                return score
            elif letter in self.three_point_letters:
                score = 3
                return score
            elif letter in self.four_point_letters:
                score = 4
                return score
            elif letter in self.five_point_letters:
                score = 5
                return score
            elif letter in self.eight_point_letters:
                score = 8
                return score
            else:
                score = 10
                return score

    def word_score(self):
        # This method adds the scores of the individual letters
        # together to create a word score
        letter_score_list = []
        for letter in self.chosen_word:
            self.letter_score(letter)
            letter_score_list.append(self.letter_score(letter))
        word_score = sum(letter_score_list)
        print(f"Your word score is {word_score}!") # Outputs the word score for user
        return word_score

    def start_round(self):
        return "Welcome to scrabble!"

    def hand_size(self):
        # Hand starts at 0 so we know to add into it
        while self.hand < 7:
            # Lets us build up the hand til we have 7 in hand
            self.tiles = random.choice(self.alphabet)  # Takes random letters from alphabet and adds them to hand
            self.tiles_in_hand.append(self.tiles)
            self.hand += 1
        print(f"Your tiles are {self.tiles_in_hand}")
        return self.hand

    def choose_word(self):
        valid_word = False # Lets us run through choose_word until the word is valid
        while not valid_word:
            self.chosen_word = input("Please choose your word.\n")
            used_letters = []
            for letter in self.chosen_word:
                used_letters.append(letter)
            if used_letters == list(filter(lambda x: x in self.tiles_in_hand, used_letters)):
                valid_word = True
            else:
                self.chosen_word = print("You don't have those tiles.")
        return self.chosen_word

    def next_round(self):
        for letter in self.chosen_word:
            if letter in self.tiles_in_hand:
                self.tiles = random.choice(self.alphabet)
                self.tiles_in_hand.remove(letter)
                self.tiles_in_hand.append(self.tiles)
        go_next = input("Would you like to play the next round?(y/n)\n").lower()
        if go_next == "y":
            self.chosen_word = " "
            self.hand_size()
            self.choose_word()
            self.word_score()
            self.next_round()
        elif go_next == "n":
            print("Thanks for the game!")
        else:
            print("That is not a valid answer, please try again.")
            go_next = input("Would you like to play the next round?(y/n)\n").lower()


game = ScrabbleGame()