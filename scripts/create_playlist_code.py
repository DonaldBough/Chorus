# Creates a playlist for a user

import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util

#System call 

username =  '1235536440'
playlist_name = 'Chorus'

#put server url for redirect url
token = util.prompt_for_user_token(username,scope,client_id='3c6df9a90b934200856b352829f09fd0',client_secret='694b8ac2f8cb478796b304fd6f1fd082',redirect_uri=''

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name)
    pprint.pprint(playlists)
else:
    print("Can't get token for", username)
