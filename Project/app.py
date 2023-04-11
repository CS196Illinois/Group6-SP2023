from flask import Flask, render_template, redirect, request, session
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)


app.secret_key = 'supersecretkey'
CLIENT_ID = '87a928e5713f44d082fdbb11eb0b8081'
CLIENT_SECRET = '609f4ce2a45943429d6905cbe8f20752'
REDIRECT_URI = 'http://localhost:5000/callback'



# set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='user-library-read'))

@app.route('/get_liked_songs')
def get_liked_songs():
    # get the user's liked songs
    results = sp.current_user_saved_tracks()
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    # create a list of tuples containing the song name, artist name, and album name
    liked_songs = []
    for item in tracks:
        track = item['track']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        album_name = track['album']['name']
        liked_songs.append((track_name, artist_name, album_name))

    # render the template with the list of liked songs
    return render_template('liked_songs.html', liked_songs=liked_songs)



@app.route('/')
def index():
    if 'access_token' in session:
        sp = spotipy.Spotify(auth=session.get('access_token'))
        user = sp.current_user()
        return f"Welcome {user['display_name']}!"
    else:
        return render_template('index.html', client_id=CLIENT_ID, redirect_uri=REDIRECT_URI)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token = util.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope='user-read-private user-read-email', cache_path='.cache').get_access_token(code)
    session['access_token'] = token['access_token']
    return redirect('/')







if __name__ == '__main__':
    app.run(debug=True)
