import random

# Board (
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Class
class Hangman:

    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    # Guess letter
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # check if finish
    def game_over(self):
        return self.player_won() or (len(self.missed_letters) == 6)

    # check if player won
    def player_won(self):
        if '_' not in self.hide_letter():
            return True
        return False

    # hide letters
    def hide_letter(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # check status and print board
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nWord: ' + self.hide_letter())
        print('\nWrong letters: ',)
        for letter in self.missed_letters:
            print(letter,)
        print()
        print('Correct letters: ',)
        for letter in self.guessed_letters:
            print(letter,)
        print()


# read random word from file
def rand_word():
    with open("words.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


def main():

    game = Hangman(rand_word())

    # print status and board until the game ends
    while not game.game_over():
        game.print_game_status()
        user_input = input('\nDType a letter: ')
        game.guess(user_input)

    # check status
    game.print_game_status()

    if game.player_won():
        print('\nCongratulations!!!')
    else:
        print('\nGame over! You lose.')
        print('The word was ' + game.word)


if __name__ == "__main__":
    main()
