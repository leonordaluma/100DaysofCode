from api_key import AV_API_KEY, News_API_KEY, account_sid, auth_token
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

stock_data = get_stock_price()
time_series = stock_data["Time Series (Daily)"]
days_list = [day for day, val in time_series.items()]
yesterday = time_series[days_list[0]]
day_before = time_series[days_list[1]]

current_stock_price = float(yesterday['4. close'])
previous_stock_price = float(day_before['4. close'])
five_percent = round(previous_stock_price * 0.05, 3)

if current_stock_price <= previous_stock_price - five_percent or current_stock_price >= previous_stock_price + five_percent:
    difference = current_stock_price - previous_stock_price
    total = difference / previous_stock_price
    percentage = total * 100
    percentage = round(percentage)
    if percentage < 0:
        percent = f"🔻{abs(percentage)}%"
        print(percent)
    else:
        percent = f"🔺{percentage}%"       
else:
    print("The stock price hasn't increased/decreased by 5%")
    
news_data = get_news()
articles = news_data["articles"][:3]

client = Client(account_sid, auth_token)
for a in articles:
    message = client.messages \
        .create(
            body=f"\n\n{STOCK}: {percent} \nHeadline: {a['title']} \nBrief: {a['description']}\n",
            from_="+18126498393",
            to="+639076469459",
        )
    print(message.status)
