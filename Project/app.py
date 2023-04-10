from flask import Flask, render_template, redirect, request, session
import spotipy
import spotipy.util as util

app = Flask(__name__)


app.secret_key = 'supersecretkey'
CLIENT_ID = '87a928e5713f44d082fdbb11eb0b8081'
CLIENT_SECRET = '609f4ce2a45943429d6905cbe8f20752'
REDIRECT_URI = 'http://localhost:5000/callback'

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
