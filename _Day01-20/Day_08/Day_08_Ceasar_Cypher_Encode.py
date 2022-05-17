alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes 
# the 'text' and 'shift' as inputs.
def encrypt(text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each 
    # letter of the 'text' forwards in the alphabet by 
    # the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the
    #  word 'civilization'?🐛
    message_list = list(text)
    # encoded_msg = []
    # for letter in message_list:
    #     letter_position = alphabet.index(letter)
    #     encoded_msg.append(alphabet[(letter_position + shift) % 26])
    encoded_msg = [alphabet[(alphabet.index(letter) + shift) % 26] for letter in message_list]
    # print(f"The encoded text is {''.join(encoded_msg)}")
    return "".join(encoded_msg)

#TODO-3: Call the encrypt function and pass in the user inputs. 
# You should be able to test the code and encrypt a message. 
print(encrypt(text, shift))