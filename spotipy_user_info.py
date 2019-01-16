import os
import sys
import json 
import webbrowser
import spotipy
import spotipy.util as util 

from json.decoder import JSONDecodeError

 #Username: 1250747227

username = sys.argv[1]
client_id = '23e4aa15bd7445eda0c9aaf36ebd7949'
secret_id = 'd8b0eb0227ef41998f707cb0ef8e1b22'
redirect_uri = 'http://localhost/'

try:
    token = util.prompt_for_user_token(username,'user-top-read playlist-read-private user-library-read',client_id,secret_id,redirect_uri)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,'user-top-read playlist-read-private user-library-read',client_id,secret_id,redirect_uri)

spotifyObj = spotipy.Spotify(auth=token)

user = spotifyObj.current_user()
top_artist = spotifyObj.current_user_top_artists(limit=100, offset=0, time_range='medium_term')
top_tracks = spotifyObj.current_user_top_tracks(limit=50, offset=0)

#print (json.dumps(user, sort_keys=True, indent=4))
#print (json.dumps(top_artist, sort_keys=True, indent=4))
#print (json.dumps(top_tracks, sort_keys=True, indent=4))

print("Popular artist in your saved song.")
for artist in top_artist['items']:
    print (artist['name'])
    genres = []
    for genre in artist['genres']:
        genres.append(genre)
    print (genres)   

print("Your top 50 songs within your liked songs.")
num = 1
for track in top_tracks['items']:
    print(num, '. ' + track['artists'][0]['name'] + ' - ' + track['name'])
    num += 1






