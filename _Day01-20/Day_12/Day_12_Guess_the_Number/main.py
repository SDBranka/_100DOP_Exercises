#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import os
from art import logo

# assigns the number of turns a player will have
def determine_turns(difficulty):
    if difficulty.lower() == "easy" or difficulty.lower() == "e":
        turns = 10
    elif difficulty.lower() == "medium" or difficulty.lower() == "m":
        turns = 5
    elif difficulty.lower() == "hard" or difficulty.lower() == "h":
        turns = 3
    return turns


# decrease turns and print the number of turns remaining
def decrease_turns(turns):
    turns -= 1
    print("Guess Again")
    print(f"You have {turns} turns left\n")
    return turns


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def guess_the_number():
    print(logo)

    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.")

    # determine difficulty
    difficulty = ""
    while difficulty.lower() != "easy" and difficulty.lower() != "medium" and difficulty.lower() != "hard" and difficulty.lower() != "e" and difficulty.lower() != "m" and difficulty.lower() != "h":
        difficulty = input("Choose a difficulty level: easy, medium, or hard: ")
    turns = determine_turns(difficulty)

    # determine computer's number
    computer_number = random.randint(1, 10)
    # computer_number = random.randint(1, 100)

    # guessing cycle
    make_guess = True
    while make_guess:
        if turns > 0:
            player_guess = int(input("Make a guess: "))
            if player_guess < computer_number:
                print("Too low")
                turns = decrease_turns(turns)
            elif player_guess > computer_number:
                print("Too high")
                turns = decrease_turns(turns)
            else:
                print("You got it!")
                print(f"Computer number is: {computer_number}\n")
                make_guess = False
        else:
            print("You ran out of turns!")
            print(f"Computer number is: {computer_number}\n")
            make_guess = False

while input("Do you want to play a number guessing game? (y/n): ") == "y":
    clear_console()
    guess_the_number()