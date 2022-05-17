import random


# Ex1
# You are going to write a virtual coin toss program. It will randomly
# tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like 
# in the example e.g. Heads, not heads.
# When you run the code, just use a random number as the seed. e.g. 67346 It 
# doesn't matter what you chose, it's only for our testing code to check your work.
# There are many ways of doing this. But to practice what we learnt in the last 
# lesson, you should generate a random number, either 0 or 1. Then use that number 
# to print out Heads or Tails.
# e.g. 1 means Heads 0 means Tails
# Example Output
# Heads
# or
# Tails

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	
# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# # 🚨 Don't change the code above 👆 It's only for testing your code.

# #Write the rest of your code below this line 👇
# # my answer which works for random coin flips, but doesn't work for random numbers
# # produce answers that work with the given test cases due to the random seed
# print(random.choice(["Heads", "Tails"]))

# # answer from the course
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")


# Ex2
# You are going to write a program that will select a random name from 
# a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them
# inside a List called names. For this to work, you must enter all the names 
# as names followed by comma then space. e.g. name, name, name
# When you run the code, just use a random number as the seed. e.g. 67346 It doesn't
# matter what you chose, it's only for our testing code to check your work.
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
# Example Output
# Michael is going to buy the meal today!
# Hint
#     You might need the help of the len() function.


# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# # print(names)
# buys_meal = random.randint(0, len(names)-1)
# print(names[buys_meal] + " is going to buy the meal today!")


# Ex3
# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested 
# list looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# In the starting code, we have used new lines (\n) to format the three rows 
# into a square, like this:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# This is to try and simulate the coordinates on a real map.

# Your job is to write a program that allows you to mark a square on the
# map using a two-digit system. The first digit is the vertical column number 
# and the second digit is the horizontal row number. e.g.:

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
column = int(position[0])
row = int(position[1])
map[row-1][column-1] = "💎"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
