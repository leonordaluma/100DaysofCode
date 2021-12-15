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
# print(sp.current_user())
user_id = sp.current_user()["id"]
# print(user_id)

date_input = input("Which year do you want to travel to? (YYYY-MM-DD): ")
url = "https://www.billboard.com/charts/hot-100/"
res = requests.get(f"{url}/{date_input}")
data = res.text

soup = BeautifulSoup(data, "html.parser")
top_100_songs = [song.getText() for song in soup.select(selector="li ul li h3", limit=100)]
tracks = []
year = date_input.split("-")[0]
# playlist = sp.user_playlist_create(
#     user = user_id,
#     name = f"{date_input} Billboard 100",
#     public = False
# )


for song in top_100_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    # try:
    #     uri = result
    
    
    
# print(playlist)
# sp.user_playlist_add_tracks(
#     user= user_id,
#     playlist_id= playlist["id"],
#     tracks=
# )