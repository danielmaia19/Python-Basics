import os
import random
import sys


# make a list of words
words = [
    "apple",
    "banana",
    "orange",
    "lime",
    "lemon",
    "melon",
    "grapefruit",
    "kumquat",
    "blueberry",
]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print("")
    print("Strikes {}/7".format(len(bad_guesses)))

    for letter in bad_guesses:
        print(letter, end='')
    print("\n\n")

    # draw spaces, letter and strikes
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
    else:
        print('_', end='')

    print("")


def get_guess(bad_guesses, good_guesses):

    while True:
        # take a guess
        guess = input("Guess a letter (there are {} letters): ".format(len(secret_word))).lower()

        if len(guess) != 1:
            print("You can only guess a letter at a time")
        elif guess in bad_guesses or guess in good_guesses:
            print("You already guessed that letter")
        elif not guess.isalpha():
            print("You can only guess letters")
        else:
            return guess

def play(done):
    clear()
    start = input("Press enter/return to start the game, or q to quit")
    if start.lower() == 'q':
        sys.exit()

    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in secret_word:
                    found = False
            if found:
                print("You Win! Congratulations")
                print("The secret word was {}".format(secret_word))
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost! ")
                print("The secret word was {}".format(secret_word))
                done = True

        if done:
            play_again = input("Would you like to play again? y/n ").lower()
            if play_again != 'n':
                return play(False)
            else:
                sys.exit()

def welcome():
    print("Welcome to letter guess game")
    start = input("Press enter/return to start the game or q to quit the game").lower()
    if start == 'q':
        sys.exit()
    else:
        play(True)


done = False


while True:
    clear()
    welcome()
    play(done)