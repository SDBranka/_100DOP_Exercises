alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):

    #TODO-2: Inside the 'decrypt' function, shift each 
    # letter of the 'text' *backwards* in the alphabet 
    # by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    message_list_d = list(cipher_text)
    decrypted_msg = []
    for letter in message_list_d:
        letter_position = alphabet.index(letter)
        decrypted_msg.append(alphabet[(letter_position - shift_amount) % 26])
    print(f"The decoded text is {''.join(decrypted_msg)}")


#TODO-3: Check if the user wanted to encrypt or decrypt
#  the message by checking the 'direction' variable. 
# Then call the correct function based on that 
# 'direction' variable. You should be able to test 
# the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)
