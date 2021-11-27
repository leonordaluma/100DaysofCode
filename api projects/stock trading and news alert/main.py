from api_key import AV_API_KEY
from datetime import datetime, time, timedelta
import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = AV_API_KEY

url = "https://www.alphavantage.co/query"
parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
    
}
response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# days = data["Time Series (Daily)"][:2]
# for dt in days:
#     print(dt["close"])

today = datetime.now()
yesterday = today - timedelta(1)
# day_before = yesterday - timedelta(1)
day_before = today - timedelta(2)
print(today)
print(yesterday)
print(day_before)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

