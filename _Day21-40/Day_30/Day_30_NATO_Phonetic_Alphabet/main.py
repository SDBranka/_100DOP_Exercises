# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    # Catch the KeyError when a user enters a character that is not in the dictionary
    except KeyError:
        # Provide feedback to the user when an illegal word was entered
        print("sorry no symbols or numbers")
        # Continue prompting the user to enter another word until they enter a valid word
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()