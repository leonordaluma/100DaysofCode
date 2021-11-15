import smtplib
import datetime as dt
import random

current_day = dt.datetime.weekday()

with open("quotes.txt") as file:
    data = file.readlines()
    quote = random.choice(data)

my_email = "myemail@gmail.com"
my_pd = "pass1234"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Good morning\n\n\n{quote}")



