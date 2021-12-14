from os import name
from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/")
contents = res.text

soup = BeautifulSoup(contents, "html.parser")
print(soup.find(name="a", class_="titlelink").getText())
# a_elements = soup.find_all(name="a", class_="titlelink")

# for a in a_elements:
#     print(a)