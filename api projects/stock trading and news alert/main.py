from api_key import AV_API_KEY, News_API_KEY, account_sid, auth_token
from datetime import datetime, time, timedelta
from twilio.rest import Client
import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = AV_API_KEY
NEWS_API_KEY = News_API_KEY
ACCOUNT_SID = account_sid
AUTH_TOKEN = auth_token

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

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def send_message():
    client = Client(account_sid, auth_token)
    news_data = get_news()
    articles = news_data["articles"][:3]
    for a in articles:
        message = client.messages \
            .create(
                body=f"\nTSLA \nHeadline: {a['title']} \nBrief: {a['description']}\n",
                from_="+18126498393",
                to="+639076469459",
            )
        print(message.status)
    
    
    
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_data = get_stock_price()
time_series = stock_data["Time Series (Daily)"]
days_list = [day for day, val in time_series.items()]
yesterday = time_series[days_list[0]]
day_before = time_series[days_list[27]]

current_stock_price = float(yesterday['4. close'])
previous_stock_price = float(day_before['4. close'])
five_percent = round(previous_stock_price * 0.05, 3)
print(current_stock_price)
print(previous_stock_price)
print(five_percent)



if current_stock_price <= previous_stock_price - five_percent:
    decrease = previous_stock_price - current_stock_price
    decrease /= round(previous_stock_price * 100, 3)
    print(f"decrease: {decrease}%") 

elif current_stock_price >= previous_stock_price + five_percent:
    increase = current_stock_price - previous_stock_price
    increase /= round(previous_stock_price * 100, 3)
    print(f"increase: {increase}%") 
    
    

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    
else:
    print("The stock price hasn't increased/decreased by 5%")



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

