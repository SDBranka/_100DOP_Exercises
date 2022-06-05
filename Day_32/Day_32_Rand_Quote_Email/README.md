# Random Quote Email

##### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)

---

## Description

This app will select a random quote from the quotes.txt file and then email it from your account to a receiver's account if the day is currently Sunday.

##### Controls

- replace my_email value with the email account you wish to mail from
    - to email from an account that is not a gmail account the SMTP_HOST value will need to be updated 
        - SMTP Information
                       gmail         hotmail             yahoo
             host  smtp.gmail.com  smtp.live.com   smtp.mail.yahoo.com

- replace my_password with the valid password for the email account you wish to mail from
- replace receiver_email with the email address you wish to mail to

##### Technologies

- Python
- smtplib
- Visual Studio

---

## How To Use

Download or clone this repository to your desktop. Run main.py in an appropriate Python environment.

- A user may need to alter their security preferences on their email account in order to allow an email to be sent by this app 

---

## References

##### Continuing Work on

- https://github.com/SDBranka/_100DOP_Exercises

\
[Back To The Top](#random-quote-email)