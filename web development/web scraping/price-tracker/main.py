import lxml
import requests
import smtplib
import time
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/ref=sr_1_1_sspa?keywords=oculus&qid=1639825393"
headers = {
'content-type': 'text/html;charset=UTF-8',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'en-US,en;q=0.8',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/56.0.2924.87 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8',
}
target_price = 100


res = requests.get(url=url, headers=headers)
data = res.text

       
        

soup = BeautifulSoup(data, "lxml")
price = float(soup.find(name="span", id="priceblock_ourprice").getText().split("$")[1])
product_name = soup.find(name="span", id="productTitle").getText()
# print(price)
# print(product_name)

my_email = ""
my_pd = ""

if price <= target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pd)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=my_email, 
                            msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now ${price}\n{url}".encode("utf-8"))