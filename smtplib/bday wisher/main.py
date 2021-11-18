##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
current_month = now.month
current_day = now.day
today = (current_month, current_day)

with open("birthdays.csv") as data:
    birthdays = pd.read_csv(data)

birthdays_dict = {(row.month, row.day): row for(index, row) in birthdays.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    name = birthday_person["name"]
    random_number = random.randint(1,3)
    with open(f"./letter_templates/letter_{random_number}.txt") as letter:
        message = letter.read()
        letter = message.replace("[NAME]",name)
        print(letter)

my_email = ""
my_pd = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pd)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=birthday_person["email"], 
        msg=f"Subject: Happy Birthday\n\n{letter}")
    
    
