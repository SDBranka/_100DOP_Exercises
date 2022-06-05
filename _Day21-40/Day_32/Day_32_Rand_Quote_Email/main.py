import smtplib
import datetime
import random

SMTP_HOST = "smtp.gmail.com"
my_email = "something@gmail.com"
my_password = "aaaaaaaa"
receiver_email = "somethingelse@yahoo.com"


# objective send a motivational quote via email on the current weekday 
# (you can change it to Monday afterwards)

# TODO Use the datetime module to obtain the current day of the week
today = datetime.datetime.now().weekday()
# print(f"today: {today}")
if today == 6:
    # TODO Open the quotes.txt file and obtain a list of quotes
    with open("quotes.txt", "r") as quotes_file:
        quotes_list = quotes_file.readlines()
        # TODO Use the random module to pick a random quote
        rand_quote = random.choice(quotes_list)
    # print(f"quotes_list: {quotes_list}")
    print(f"rand_quote: {rand_quote}")

    # TODO use the smtblib to send the email to yourself
    # create connection object
    with smtplib.SMTP(SMTP_HOST) as connection:
        # start transport layer security - encryption
        connection.starttls()
        # login to email
        connection.login(user=my_email, password=my_password)
        # send email
        connection.sendmail(from_addr=my_email, 
                            to_addrs=receiver_email,
                            # subject = "Motivational Quote", \n\n breaks subject from body of the email
                            msg=f"Subject:Motivational Quote\n\n{rand_quote}"
        )


