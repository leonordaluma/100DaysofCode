from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read() 


soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag)
#     print(tag.getText())
#     print(tag.get("href"))

print(soup.find(name="h1", id="name"))
print(soup.find(name="h3", class_="heading" ))


