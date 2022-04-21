#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program lets you play a number guessing game
#   with user input


import random


def main():
    # this program starts the game

    some_variable = random.randint(0, 9)  # a number between 0 & 9
    guess_counter = 1
    guess = 0

    # input

    while guess != some_variable:
        guess = input("\nEnter a guess (between 0 & 9): ")  # a number between 0 & 9
        try:
            guess_int = int(guess)

            # process & output

            if guess_int == some_variable:
                print(
                    "\nCorrect! You guessed the right number after {} tries.".format(
                        guess_counter
                    )
                )
                break
            elif guess_int < 0 or guess_int > 9:
                print("\nUndefined")
                guess_counter = guess_counter + 1
            else:
                print("\nYou guessed incorrectly. Try again?")
                guess_counter = guess_counter + 1
        except Exception:
            print("\nThis was not an integer")
            guess_counter = guess_counter + 1


if __name__ == "__main__":
    main()
