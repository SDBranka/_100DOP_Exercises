#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
turns = 3
while "_" in display and turns > 0:
    print(f"You have {turns} turns left.")
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    if guess not in chosen_word or guess in display:
        print("Try again.")
        turns -= 1
    else:
        for i in range(word_length):
            letter = chosen_word[i]
            # print(f"Current i: {i}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[i] = letter
    print(display)
    print("\n")

if turns > 0:
    print("You won!")
else:
    print("You lost!")
    



