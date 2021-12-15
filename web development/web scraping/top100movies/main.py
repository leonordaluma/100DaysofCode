from bs4 import BeautifulSoup
import requests
import json


res = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
contents = res.text
soup = BeautifulSoup(contents, "html.parser")

data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])
# print(json.dumps(titles, indent=4))
all_movies = []
def find_articles(data):
    if isinstance(data, dict):
        for k, v in data.items():
            if k.startswith("ImageMeta:"):
                yield v["titleText"]
            else:
                yield from find_articles(v)
    elif isinstance(data, list):
        for i in data:
            yield from find_articles(i)


for a in find_articles(data):
    all_movies.append(a)

movies_desc = all_movies[::-1]
print(movies_desc)