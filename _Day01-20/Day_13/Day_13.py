# Ex1
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# Fix the code so that it works and passes the tests when you submit.
# Hint
#   Review the previous lesson and go through the 10 steps to tackle 
#   these debugging problems.

# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# number = int(input("Which number do you want to check?"))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


# Ex2
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.

# Fix the code so that it works and when you hit submit it should pass all the tests.

# year = input("Which year do you want to check?")

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")


# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")


# Ex3
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# The code needs to print the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# Hint
# There is more than one fix required.

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)









