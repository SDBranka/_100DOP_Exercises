import random
import pandas


name = "Angela"

letters_list = [letter for letter in name[1:5]]
print(f"letters_list: {letters_list}\n")

let_list = list(name)
print(f"let_list: {let_list}\n")

doubled_nums = [num * 2 for num in range(1, 5)]
print(f"doubled_nums: {doubled_nums}\n")

names = ["Angela", "Bob", "Cindy", "Derek", "Eve", "Tina"]
short_names = [name for name in names if len(name) < 5]
print(f"short_names: {short_names}\n")

long_names_cap = [name.upper() for name in names if len(name) > 5]
print(f"long_names_cap: {long_names_cap}\n")

# Dictionary Comprehension
# new_dict0 = {new_key:new_value} for item in list}
# new_dict1 = {new_key:new_value for (key, value) in dict.items()}

# create a dictionary of students and a random score from names 
student_scores = {name:random.randint(0, 101) for name in names}
print(f"student_scores: {student_scores}\n")

# create a dictionary of students with scores over 60 from student_scores dictionary
passed_students = {student:score for (student, score) in student_scores.items() if score > 60}
print(f"passed_students: {passed_students}\n")


student_dict = {
    "student": ["Angela", "Bob", "Cindy", "Derek", "Eve", "Tina"],
    "score": [random.randint(0, 101) for _ in range(6)]
}

# # looping through a dictionary
# for (key, value) in student_dict.items():
#     print(f"key: {key}")
#     print(f"value: {value}")

# iterate over a pandas dataframe
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)
print("\n")

for index, row in student_dataframe.iterrows():
    # print(f"index: {index}")
    # print(f"{row}")
    # print(f"row.student: {row['student']}")
    # print(f"row.score: {row['score']}")
    if row.student == "Angela":
        print(f"Angela's score: {row.score}")
        print(f"Angela's index: {index}")











