
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='<87a928e5713f44d082fdbb11eb0b8081>',
                                               client_secret='<609f4ce2a45943429d6905cbe8f20752>',
                                               redirect_uri='http://localhost:5000/callback',
                                               scope='user-library-read'))

# get the user's liked songs
results = sp.current_user_saved_tracks()
tracks = results['items']

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# extracts the URL of each liked song
song_urls = [track['track']['external_urls']['spotify'] for track in tracks]

# store the URLs in a file
with open('liked_song_urls.txt', 'w') as f:
    for url in song_urls:
        f.write(url + '\n')