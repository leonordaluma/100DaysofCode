import lxml
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/ref=sr_1_1_sspa?keywords=oculus&qid=1639825393"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53"
accept_lang = "en-US,en;q=0.9"

res = requests.get(url=url, headers={
    "User-Agent": user_agent,
    "Accept-Language": accept_lang
})
print(res.text)