from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/")
contents = res.text

