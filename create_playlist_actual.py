import pprint
import sys
import spotipy
import spotipy.util as util

#refresh_access_token(
#Creates a playlist for a user
#need username id from database
#username = 

playlist_name = 'Chorus'
scope = 'playlist-read-private playlist-read-collaborative playlist-modify-private'

#put server url for redirect url
token = util.prompt_for_user_token(username,scope,client_id='3c6df9a90b934200856b352829f09fd0',client_secret='694b8ac2f8cb478796b304fd6f1fd082',redirect_uri='http://localhost/')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name)
    pprint.pprint(playlists)
    return token

else:
    print("Can't get token for", username)
    return 0;
