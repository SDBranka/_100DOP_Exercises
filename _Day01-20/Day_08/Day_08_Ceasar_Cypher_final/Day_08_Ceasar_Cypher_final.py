# TODO-1: Import and print the logo from art.py when 
# the program starts.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    stated_direction = "encoded"
    if cipher_direction.lower() == "decode" or cipher_direction.lower() == "d" or cipher_direction.lower() == "encode" or cipher_direction.lower() == "e":
        if cipher_direction.lower() == "decode" or cipher_direction.lower() == "d":
            shift_amount *= -1
            stated_direction = "decoded"
        for char in start_text:
            # TODO-3: What happens if the user enters a 
            # number/symbol/space?
            # Can you fix the code to keep the 
            # number/symbol/space when the text is 
            # encoded/decoded?
            #e.g. start_text = "meet me at 3"
            #end_text = "•••• •• •• 3"
            if char.isalpha():
                position = alphabet.index(char)
                # TODO-2: What if the user enters a shift that is greater
                # than the number of letters in the alphabet?
                # Try running the program and entering a shift number of
                # 45.
                # Add some code so that the program continues to work 
                # even if the user enters a shift number greater than 26.
                # Hint: Think about how you can use the modulus (%).
                new_position = (position + shift_amount) % 26
                end_text += alphabet[new_position]
            else:
                end_text += char

        print(f"Here's the {stated_direction} result: {end_text}\n")
    else:
        print("invalid input")

# TODO-4: Can you figure out a way to ask the user if
#  they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise 
# type 'no'.
# If they type 'yes' then ask them for the 
# direction/text/shift again and call the caesar() 
# function again?
# Hint: Try creating a while loop that continues to 
# execute the program if the user types 'yes'.
go_again = 'yes'

while go_again.lower() == 'yes' or go_again.lower() == 'y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
        



