
# ex1
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# ex2
# works like ex1, but without the close()
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# ex3
# writing to a file
with open("my_file.txt", "w") as file:
    file.write("Hello World!")

# ex4
# appending to a file
with open("my_file.txt", "a") as file:
    file.write("\nHello Again!")

# ex5
# creating a new file to write to
#     enter the name of the new file to 
#     write to and it will be created
with open("my_file0.txt", "w") as file:
    file.write("New file created!")

# ex6
# use a relative path to open a file
with open("../Day_24_Snake_Game/data.txt") as file:
    contents = file.read()
    print(contents)

