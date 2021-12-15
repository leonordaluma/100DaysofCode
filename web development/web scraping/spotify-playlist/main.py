import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from keys import client_id, client_secret


ID = client_id
SECRET = client_secret

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=ID,
        client_secret=SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
date_input = input("Which year do you want to travel to? (YYYY-MM-DD): ")
url = "https://www.billboard.com/charts/hot-100/"
res = requests.get(f"{url}/{date_input}")
data = res.text

soup = BeautifulSoup(data, "html.parser")
top_100_songs = [song.getText() for song in soup.select(selector="li ul li h3", limit=100)]
