# Ex1
# You are going to write a List Comprehension to create a new list called 
# squared_numbers. This new list should contain every number in the list 
# numbers but each number should be squared.
# e.g. 
# 4 * 4 = 16
# 4 squared equals 16.
# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.
# Example Output
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
# Hint
# Use the keyword method for starting the List comprehension and fill in the relevant parts.
# Make sure the squared_numbers is printed into the console for the code checking to work.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
#Write your 1 line code 👇 below:
squared_numbers = [number ** 2 for number in numbers]
#Write your code 👆 above:

# print(squared_numbers)


# Ex2
# You are going to write a List Comprehension to create a new list 
# called result. This new list should only contain the even numbers 
# from the list numbers.
# DO NOT modify the List numbers directly. Try to use List Comprehension
# instead of a Loop.
# Example Output
# [2, 8, 34]
# Hint
#     Use the keyword method for starting the List comprehension and fill
#     in the relevant parts.
#     Even numbers can be divided by 2 with no remainder.
#     Remind yourself of how the modulo operator works.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above
#Write your 1 line code 👇 below:
result = [number for number in numbers if number % 2 == 0]
#Write your code 👆 above:
# print(result)


# Ex3
# Take a look inside file1.txt and file2.txt. They each contain a
# bunch of numbers, each number on a new line.
# You are going to create a list called result which contains 
# the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
# and file2.txt contained:
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The result should be a list that contains Integers, 
# not Strings. Try to use List Comprehension instead of a Loop.
# Example Output
# [3, 6, 5, 33, 12, 7, 42, 13]
# Hint
#     Use the keyword method for starting the List comprehension 
#       and fill in the relevant parts.
#     First, you will need to read from the files and create a 
#       list using the lines in the files.
#     This method will be really useful: 
#       https://www.w3schools.com/python/ref_file_readlines.asp
#     Remember you can check if a value exists in a list using the in 
#       keyword. https://www.w3schools.com/python/ref_keyword_in.asp
#     Remember you can convert a string to an int using the int() 
#       method. https://www.w3schools.com/python/ref_func_int.asp

f1 = open("file1.txt", "r")
# print(f1.readlines())
f1_list = f1.readlines()
f2 = open("file2.txt", "r")
# print(f2.readlines()) 
f2_list = f2.readlines()
result = [int(num) for num in f1_list if num in f2_list]
# Write your code above 👆

# print(result)


# Ex4
# You are going to use Dictionary Comprehension to create a
# dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a 
# list of words.
# Do NOT Create a dictionary directly. Try to use Dictionary 
# Comprehension instead of a Loop.
# Example Output
# {
# 'What': 4, 
# 'is': 2, 
# 'the': 3, 
# 'Airspeed': 8, 
# 'Velocity': 8, 
# 'of': 2, 
# 'an': 2, 
# 'Unladen': 7, 
# 'Swallow?': 8
# }
# Hint
# Use the keyword method for starting the Dictionary comprehension
#  and fill in the relevant parts.
# You can get a list of the words in a string by using the .split() 
# method: https://www.w3schools.com/python/ref_string_split.asp

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word:len(word) for word in sentence.split()}

# print(result)

