from art import logo, vs
from game_data import data
import random
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Game Cycle
user_score = 0

compare_a = random.choice(data)
# print(compare_a)

play_round = True
while play_round:
    print(logo)
    if user_score > 0:
        print(f"You're right! Current score: {user_score}")

    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")

    print(vs)

    compare_b = random.choice(data)
    # print(compare_b)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.\n")

    # make selection and restrict player to "a" or "b"
    user_choice = ""
    while user_choice != "a" and user_choice != "b":
        user_choice = input("Who has more followers? Type A or B: ")
        user_choice = user_choice.lower()

    if user_choice == "a":
        if compare_a['follower_count'] > compare_b['follower_count']:
            print("You are correct")
            user_score += 1
        else:
            play_round = False 
    else:
        if compare_a['follower_count'] < compare_b['follower_count']:
            print("You are correct")
            user_score += 1
            compare_a = compare_b
        else:
            play_round = False

clear_console()
print(logo)
print("You are incorrect")
print(f"Your final score is: {user_score}")
