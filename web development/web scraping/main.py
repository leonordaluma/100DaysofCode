from os import name
from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/")
contents = res.text

soup = BeautifulSoup(contents, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for tag in articles:
    text = tag.getText()
    article_texts.append(text)
    link = tag.get("href")
    article_links.append(link)
    
article_scores = [score.getText() for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_scores)