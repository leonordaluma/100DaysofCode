from api_key import AV_API_KEY, News_API_KEY
from datetime import datetime, time, timedelta
import math
import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = AV_API_KEY
NEWS_API_KEY = News_API_KEY

def get_stock_price():
    url = "https://www.alphavantage.co/query"
    parameters = {
        "function" : "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
        
    }
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    return response.json()

def get_news():
    url = "https://newsapi.org/v2/everything"
    parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    return response.json()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_data = get_stock_price()
time_series = stock_data["Time Series (Daily)"]
days_list = [day for day, val in time_series.items()]
yesterday = time_series[days_list[0]]
day_before = time_series[days_list[27]]

current_stock_price = float(yesterday['4. close'])
previous_stock_price = float(day_before['4. close'])
print(f"previous: {previous_stock_price}")
print(f"current: {current_stock_price}")
five_percent = round(previous_stock_price * 0.05, 3)
print(five_percent)
if current_stock_price <= previous_stock_price - five_percent or current_stock_price >= previous_stock_price + five_percent:
    print("Get News")
else:
    print("The stock price hasn't increased/decreased by 5%")
    
    
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_data = get_news()
articles = news_data["articles"]
news_pieces = articles[:3]
print(news_pieces[1])


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

