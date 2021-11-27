from api_key import AV_API_KEY
from datetime import datetime, time, timedelta
import math
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

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
time_series = data["Time Series (Daily)"]
days_list = [day for day, val in time_series.items()]
yesterday = time_series[days_list[0]]
day_before = time_series[days_list[1]]

current_stock_price = float(yesterday['4. close'])
previous_stock_price = float(day_before['4. close'])
print(f"previous: {previous_stock_price}")
print(f"current: {current_stock_price}")
five_percent = current_stock_price * 0.05
print(round(five_percent, 3))
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

