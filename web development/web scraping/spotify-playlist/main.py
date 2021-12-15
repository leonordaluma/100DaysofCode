import requests
from bs4 import BeautifulSoup
from keys import client_id, client_secret


ID = client_id
SECRET = client_secret

date_input = input("Which year do you want to travel to? (YYYY-MM-DD): ")
url = "https://www.billboard.com/charts/hot-100/"
res = requests.get(f"{url}/{date_input}")
data = res.text

soup = BeautifulSoup(data, "html.parser")
top_100_songs = [song.getText() for song in soup.select(selector="li ul li h3", limit=100)]
print(len(top_100_songs))
print(top_100_songs)