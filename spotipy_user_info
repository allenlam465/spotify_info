import os
import sys
import json 
import webbrowser
import spotipy
import spotipy.util as util 

from json.decoder import JSONDecodeError

username = sys.argv[1]
client_id = '23e4aa15bd7445eda0c9aaf36ebd7949'
secret_id = 'd8b0eb0227ef41998f707cb0ef8e1b22'
redirect_uri = 'http://localhost/'

try:
    token = util.prompt_for_user_token(username,'user-top-read',client_id,secret_id,redirect_uri)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,'user-top-read',client_id,secret_id,redirect_uri)

spotifyObj = spotipy.Spotify(auth=token)

user = spotifyObj.current_user()
top_artist = spotifyObj.current_user_top_artists(limit=20, offset=0, time_range='medium_term')

#print (json.dumps(user, sort_keys=True, indent=4))
#print (json.dumps(top_artist, sort_keys=True, indent=4))

for item in top_artist['items']:
    print (item['name'])
    for genre in item['genres']:
        print (genre)



