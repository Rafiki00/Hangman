# This is the classic Hangman game
from hanged import hanged
import getpass

class Word:

    def __init__(self, word):
        self.word = word
        self.length = len(self.word)

    def get_length(self):
        return self.length


class Game:

    def __init__(self, word):
        self.word = Word(word)
        self.letters_guessed = []
        self.letters_failed = []
        self.wrong_guesses = 0
        self.display()

    def guess_letter(self):
        while True:
            letter = input("Choose a letter or guess the word!").upper()
            if type(letter) == str and len(letter) == 1:
                break
            elif letter == self.word.word:
                print("You guessed it !")
                quit()
            else:
                print("Choose a valid letter")
        if letter in self.word.word:
            self.letters_guessed.append(letter)
        elif letter not in self.word.word and letter not in self.letters_failed:
            self.letters_failed.append(letter)
            self.wrong_guesses += 1
            if self.wrong_guesses == 7:
                print("You have run out of attempts ! (X_X) ")
                quit()
        else:
            print("Letter already guessed !")
        self.display()

    def display(self):
        displayed_word = ""
        for i in range(self.word.length):
            displayed_word += " "
            if self.word.word[i] in self.letters_guessed:
                displayed_word += self.word.word[i]
            elif self.word.word[i] == " ":
                displayed_word += " "
            else:
                displayed_word += "_"
        print(hanged[self.wrong_guesses])
        print(displayed_word)
        print("Wrong guesses: ", self.letters_failed)
        if "_" not in displayed_word:
            print("You guessed it !")
        else:
            self.guess_letter()


def initialize():
    while True:
        starting = getpass.getpass(prompt="Choose a word, don't let the other players see !").upper()
        if type(starting) == str and len(starting) > 0:
            break
        else:
            print("Choose a word or phrase with a length of more than 0")
    new_game = Game(starting)

print(type("a"))
initialize()
print(len([1, 2, 3, 4, 5]))
