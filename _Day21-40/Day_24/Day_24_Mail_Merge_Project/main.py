#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as file:
    ex_letter = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

# print(names)

# for each name in names replace to_be_replaced with name
for name in names:
    new_letter = ex_letter.replace(PLACEHOLDER, name.strip())
    # print(new_letter)
    with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as completed_letter:
        completed_letter.write(new_letter)