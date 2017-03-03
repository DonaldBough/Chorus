import pprint
import sys

import spotipy
import spotipy.util as util

username = '1235536440'

track_ids = '2gFvRmQiWg9fN9i74Q0aiw 4Km5HrUvYTaSUfiSGPJeQR 7BKLCZ1jbUBVqRi2FVlTVw 3bi8yEuK44vLcbjHkPH0u1 5SDVX9gpSXoE0M6KZt4EBF 0O6jl8Zamz6TGF0nUwMQsF 4RnfMhMUMqHlrn4V6A3KfS 6F5c58TMEs1byxUstkzVeM 3cfOd4CMv2snFaKAnMdnvK'

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username,scope,client_id='3c6df9a90b934200856b352829f09fd0',client_secret='694b8ac2f8cb478796b304fd6f1fd082',redirect_uri='')

sp = spotipy.Spotify(auth=token)
sp.trace = False

# find album by name
name = "Chorus"
playlists = sp.user_playlists(username, limit=50, offset=0)

# get the first album uri
for playlist in playlists['items']:
    if(playlist['name'] == name):
        playlist_id = playlist['id']


sp.user_playlist_add_tracks(username, playlist_id, track_ids)
print("playlist id: " + playlist_id)
