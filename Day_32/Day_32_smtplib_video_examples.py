import smtplib


# connection = smtplib.SMTP(host)
# SMTP Information
#           gmail         hotmail             yahoo
# host  smtp.gmail.com  smtp.live.com   smtp.mail.yahoo.com


# # create connection object
# connection = smtplib.SMTP("smtp.gmail.com")

# # start transport layer security - encryption
# connection.starttls()
# connection.login(user=my_email, password=password)

# # send email
# connection.sendmail(from_addr=my_email, 
#                     to_addrs="another@gmail.com",
#                     # subject = "Hello", \n\n breaks subject from body of the email
#                     msg="Subject:Hello\n\nThis is the body of my email."
# )

# # close the connection
# connection.close()

# or can do

# with smtplib.SMTP("smtp.gmail.com") as connection:
# # create connection object
#     # start transport layer security - encryption
#     connection.starttls()
#     connection.login(user=my_email, password=password)

#     # send email
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="another@gmail.com",
#                         # subject = "Hello", \n\n breaks subject from body of the email
#                         msg="Subject:Hello\n\nThis is the body of my email."
#     )








