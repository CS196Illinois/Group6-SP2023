import pandas as pd 
import pip._vendor.requests as requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
scope1 = "user-library-read"
from spotipy.oauth2 import SpotifyClientCredentials
sp =spotipy.Spotify(auth_manager= SpotifyOAuth(client_id = "15fd015d4da742d0bf7da9c6ed3120c7", client_secret = "349c5181636e4e3cbb974b051db425fd", redirect_uri = "http://mysite.com/callback/", scope= scope1))

devil_url = "spotify:artist:06HL4z0CvFAxyc27GXpf02"
results = sp.artist_albums(devil_url, album_type= "album")
albums = results['items']
while results['next']: 
    results = sp.next(results) 
    albums.extend(results["items"])
data = []

for album in albums :
    d = {"album" : album["name"]}
    data.append(d)
    print(album["name"])

df = pd.DataFrame(data)
df
