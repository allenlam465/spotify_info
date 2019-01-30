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
scope = 'user-top-read playlist-read-private user-library-read user-library-modify playlist-modify-public playlist-modify-private'

try:
    token = util.prompt_for_user_token(username, scope,client_id,secret_id,redirect_uri)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id,secret_id,redirect_uri)

spotifyObj = spotipy.Spotify(auth=token)

user = spotifyObj.current_user()
top_artist = spotifyObj.current_user_top_artists(limit=100, offset=0, time_range='long_term')
top_tracks = spotifyObj.current_user_top_tracks(limit=50, offset=0, time_range='long_term')
playlists = spotifyObj.current_user_playlists()

playlist_name = input("What is the playlist name? \n>")
exist = False

for pl in playlists['items']:
    if pl['name'] == playlist_name:
        exist = True
        top_playlist = pl
        break

if not exist:
    top_playlist = spotifyObj.user_playlist_create(username, playlist_name, public=False)
else:
    top_playlist = spotifyObj.user_playlist_create(username, "Your Top Tracks", public=False)

track_list = []
for track in top_tracks['items']:
    track_list.append(track['id'])

results = spotifyObj.user_playlist_add_tracks(username, top_playlist['id'], track_list)






