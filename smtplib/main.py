# import smtplib

# my_email = 'name@email.com'
# password = 'password123'

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="receiver@yahoo.com",
#         msg="Subject:New Message\n\nThis is the body of my email."
#     )

import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
print(year)
month = now.month
day_of_week = now.weekday()
print(day_of_week)

dob = dt.datetime(year=1999, month=5, day=12)
print(dob.year)