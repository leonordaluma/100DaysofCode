import smtplib
import datetime as dt
import random

current_day = dt.datetime.now()
weekday = current_day.weekday()
my_email = ""
my_pd = ""


if weekday == 2:
    with open("quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)
    
    print(quote)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pd)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Good morning\n\n{quote}")



