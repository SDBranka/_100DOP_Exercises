import smtplib
import datetime
import pandas
import random


PLACEHOLDER = "[NAME]"
SMTP_HOST = "smtp.gmail.com"
MY_EMAIL = "something@gmail.com"
MY_PASSWORD = "aaaaaaaa"


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
today_date, today_month = today.day, today.month
print(f"today_date: {today_date}, today_month: {today_month}")

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")
# print(f"birthday_data: \n{birthday_data}")
# print(f"birthday_dict: \n{birthday_dict}")

bdays_today = []
for person in birthday_dict:
    if person["day"] == today_date and person["month"] == today_month:
        # print(person)
        bdays_today.append(person)
# print(f"bdays_today:\n{bdays_today}")

# 3. If step 2 is true, pick a random letter from letter templates and replace 
# the [NAME] with the person's actual name from birthdays.csv
with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
    bday_letter = file.read()

for bday in bdays_today:
    # for each bday in bdays_today replace PLACEHOLDER with 
    # name of the person
    new_letter = bday_letter.replace(PLACEHOLDER, bday["name"])
    # print(new_letter)
    # with open(f"ReadyToSend/letter_for_{bday['name']}.txt", "w") as completed_letter:
    #     completed_letter.write(new_letter)    
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP(SMTP_HOST) as connection:
        # start transport layer security - encryption
        connection.starttls()
        # login to email
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        # send email
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=bday["email"],
                            # subject = "HAPPY BIRTHDAY!!!", \n\n breaks subject from body of the email
                            msg=f"Subject:HAPPY BIRTHDAY!!!\n\n{new_letter}"
        )





