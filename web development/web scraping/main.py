from os import name
from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/")
contents = res.text

soup = BeautifulSoup(contents, "html.parser")
article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_score = soup.find(name="span", class_="score").getText()
print(article_link)
print(article_score)
# a_elements = soup.find_all(name="a", class_="titlelink")

# for a in a_elements:
#     print(a)