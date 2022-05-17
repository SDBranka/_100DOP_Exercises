import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# can't use choice as per assignment
# print(random.choice(names))

print(f"{names[random.randint(1, len(names)) - 1]} is going to pay the bill.")
