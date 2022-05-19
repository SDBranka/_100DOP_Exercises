student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(f"key: {key} | value: {value}")
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    student = row.student
    score = row.score
    # print(f"student: {student}, score: {score}")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alpha_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter:row.code for index, row in alpha_data.iterrows()}
# print(f"alpha_dict: {alpha_dict}\n")


#TODO 2. Create a list of the phonetic code words 
# from a word that the user inputs.
user_word = (input("Enter a word: ")).upper()
coded_word = [alpha_dict[letter] for letter in user_word]
print(f"coded_word: {coded_word}")







