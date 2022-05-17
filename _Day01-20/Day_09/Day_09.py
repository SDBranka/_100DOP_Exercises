# Ex1
# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are 
# their exam scores.
# Write a program that converts their scores to grades. By the end of your 
# program, you should have a new dictionary called student_grades that should 
# contain student names for keys and their grades for values. The final version 
# of the student_grades dictionary will be checked.
# DO NOT modify lines 1-7 to change the existing student_scores dictionary.
# DO NOT write any print statements.
# This is the scoring criteria:
#     Scores 91 - 100: Grade = "Outstanding"
#     Scores 81 - 90: Grade = "Exceeds Expectations"
#     Scores 71 - 80: Grade = "Acceptable"
#     Scores 70 or lower: Grade = "Fail"
# Expected Output
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
# Hint
# Remember that looping through a Dictionary will only give you 
# the keys and not the values.
# If in doubt as to why your code is not doing what you expected, you can 
# always print out the intermediate values.
# At the end of your program, the print statement will show the final student_scores 
# dictionary, do not change this.

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
# print(student_grades)


# Ex2
# You are going to write a program that adds to a travel_log. You can see a 
# travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add 
# the entry for Russia to the travel_log.
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#     You've visited Russia 2 times.
#     You've been to Moscow and Saint Petersburg.
# DO NOT modify the travel_log directly. You need to create a function that modifies it.
# Hint
# Look at the function call above to see what the name of the function should be.
# The inputs for the function are positional arguments. The order is very important.
# Feel free to choose your own parameter names.

travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

# mine
def add_new_country0(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})

# theirs
def add_new_country(name, visit_count, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = visit_count
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
