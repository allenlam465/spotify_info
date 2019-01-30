import os
import sys
import json 
import webbrowser
import spotipy
import spotipy.util as util 

from spotipy.oauth2 import SpotifyClientCredentials
from json.decoder import JSONDecodeError

#Username: 1250747227

def long_term_playlist(spotify_object):
    top_tracks = spotify_object.current_user_top_tracks(limit=50, offset=0, time_range='long_term')
    playlists = spotify_object.current_user_playlists()

    playlist_name = input("What is the playlist name? \n>")
    exist = False

    for pl in playlists['items']:
        if pl['name'] == playlist_name:
            exist = True
            top_playlist = pl
            break

    if not exist:
        top_playlist = spotify_object.user_playlist_create(username, playlist_name, public=False)

    track_list = []
    for track in top_tracks['items']:
        track_list.append(track['id'])

    spotify_object.user_playlist_add_tracks(username, top_playlist['id'], track_list)


username = sys.argv[1]

client_id = os.getenv('SPOTIPY_CLIENT_ID')
secret_id = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

scope = 'user-top-read playlist-read-private user-library-read user-library-modify playlist-modify-public playlist-modify-private'

try:
    token = util.prompt_for_user_token(username, scope, client_id, secret_id, redirect_uri)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id, secret_id, redirect_uri)

spotify_object = spotipy.Spotify(auth=token)

user = spotify_object.current_user()

long_term_playlist(spotify_object)