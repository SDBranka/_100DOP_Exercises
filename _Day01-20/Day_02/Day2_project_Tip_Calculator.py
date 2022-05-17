#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some
#     Googling to solve this.💪

#Write your code below this line 👇
def calculate_tip(bill_amount, tip):
    tip = bill_amount * tip / 100
    return tip

def split_bill(bill_amount, num_people, tip):
    total_bill = bill_amount + calculate_tip(bill_amount, tip)
    return round(total_bill / num_people, 2)

print("Welcome to Tip Calculator!")
user_bill = float(input("What is the bill amount? "))
user_tip = float(input("What is the tip percentage? "))
user_people = int(input("How many people are splitting the bill? "))
print("Each person should pay: $" + str(split_bill(user_bill, user_people, user_tip)))
