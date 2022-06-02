# FileNotFound error
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existant_key"]

# IndexError
# fruit_list = ["apple", "orange", "pear"]
# fruit = fruit_list[5]

# TypeError
# text = "abc"
# print(text + 5)

# try - something that might cause an exception
# except - do this if there was an exception
# else - do this if there were no exceptions
# finally - do this no matter what happens

# FileNotFound error corrected
# with open("a_file.txt") as file:
#     file.read()
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    # print(a_dictionary["hat"])
    print(a_dictionary["key"])
# catches FileNotFound errors
except FileNotFoundError:
    print("No such file exists")
    file = open("a_file.txt", "w")
    file.write("Something")
# catches KeyError instances and prints the key in question
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    # forces a KeyError regardless of actual condition and prints message
    # raise KeyError("This is an error that I made up")
    file.close()
    print("File was closed")










