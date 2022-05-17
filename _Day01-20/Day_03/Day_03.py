# Ex1
# Write a program that works out whether if a given number is an odd or even number.

# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if int(number) % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an even number")

# print("This is an even number" if number % 2 == 0 else "This is an odd number")


# Ex2
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

#     Under 18.5 they are underweight
#     Over 18.5 but below 25 they have a normal weight
#     Over 25 but below 30 they are slightly overweight
#     Over 30 but below 35 they are obese
#     Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# bmi = weight / (height * height)
# if bmi < 18.5:
#     diagnosis = "you are underweight"
# elif bmi < 25:
#     diagnosis = "you have a normal weight"
# elif bmi < 30:
#     diagnosis = "you are slightly overweight"
# elif bmi < 35:
#     diagnosis = "you are obese"
# else:
#     diagnosis = "you are clinically obese"
# print(f"Your BMI is {round(bmi)}, {diagnosis}")


# Ex3
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# The reason why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE
# This is how you work out whether if a particular year is a leap year.
#     on every year that is evenly divisible by 4 
#     **except** every year that is evenly divisible by 100 
#     **unless** the year is also evenly divisible by 400
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)
# Warning your output should match the Example Output format exactly, even the 
# positions of the commas and full stops.

# Example Input 1
# 2400
# Example Output 1
# Leap year.

# Example Input 2
# 1989
# Example Output 2
# Not leap year.

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")


# Ex4
# Congratulations, you've got a job at Python Pizza. Your first job is to build 
# an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.


# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# total_bill = 0
# if size == "S":
#     total_bill += 15
# elif size == "M":
#     total_bill += 20
# else:
#     total_bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         total_bill += 2
#     else:
#         total_bill += 3

# if extra_cheese == "Y":
#     total_bill += 1

# print(f"Your final bill is: ${total_bill}.")


# Ex5
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
#     Take both people's names and check for the number of times the letters
#       in the word TRUE occurs. 
#     Then check for the number of times the letters in the word LOVE occurs. 
#     Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1, name2 = name1.lower(), name2.lower()
# true_count = 0
# love_count = 0

# for char in "true":
#     true_count += name1.count(char) + name2.count(char)
# for char in "love":
#     love_count += name1.count(char) + name2.count(char)

# # print(f"true_count: {true_count}")
# # print(f"love_count: {love_count}")

# truelove_score = int(str(true_count) + str(love_count))
# # print(f"truelove_score: {truelove_score}")
# # print(f"truelove type: {type(truelove_score)}")
# if truelove_score < 10 or truelove_score > 90:
#     print(f"Your score is {truelove_score}, you go together like coke and mentos.")
# elif truelove_score >= 40 and truelove_score <= 50:
#     print(f"Your score is {truelove_score}, you are alright together.")
# else:
#     print(f"Your score is {truelove_score}.")