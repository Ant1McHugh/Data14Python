from scrabble import ScrabbleGame

game_test = ScrabbleGame()


def test_letter_score():
    assert game_test.letter_score("a") == 1
    assert game_test.letter_score("g") == 2
    assert game_test.letter_score("b") == 3
    assert game_test.letter_score("v") == 4
    assert game_test.letter_score("k") == 5
    assert game_test.letter_score("x") == 8
    assert game_test.letter_score("z") == 10


def test_word_score():
    assert game_test.word_score() == 5
    assert game_test.word_score() == 7
    assert game_test.word_score() == 14


def test_hand_size():
    assert game_test.hand_size() == 7
