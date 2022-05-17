import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors? "))
computer_choice = random.randint(0, 2)
game_options = [rock, paper, scissors]


if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Game over.")
else:
    print("User throws: \n" + game_options[user_choice])
    print("Computer throws: \n" + game_options[computer_choice])

    if (user_choice == "0" and computer_choice == 0) or (user_choice == "1" and computer_choice == 1) or (user_choice == "2" and computer_choice == 2):
        print("It's a tie!")
    elif (user_choice == "0" and computer_choice == 1) or (user_choice == "1" and computer_choice == 2) or (user_choice == "2" and computer_choice == 0):
        print("You win!")
    else:
        print("You lose!")

