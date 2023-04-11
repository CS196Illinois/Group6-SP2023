import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

client_id = "87a928e5713f44d082fdbb11eb0b8081"
client_secret = "609f4ce2a45943429d6905cbe8f20752"
redirect_uri = "http://localhost:5000/callback"

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-library-read")

#  user's authorization
auth_url = sp_oauth.get_authorize_url()
print(auth_url)
response = input("Paste the URL you were redirected to: ")
code = sp_oauth.parse_response_code(response)

#  access token for the user
token_info = sp_oauth.get_access_token(code)

# use the access token to authenticate with the Spotify API
sp = spotipy.Spotify(auth=token_info['access_token'])

# get the user's liked songs
results = sp.current_user_saved_tracks()

# store the song information in a list
songs = []
for item in results['items']:
    track = item['track']
    song = {
        'id': track['id'],
        'name': track['name'],
        'artist': track['artists'][0]['name'],
        'album': track['album']['name']
    }
    songs.append(song)

# Print the list of songs
print(songs)
