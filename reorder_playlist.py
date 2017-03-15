import pprint
import sys
import spotipy
import spotipy.util as util

sp = spotipy.Spotify(auth=token)
sp.trace = False

#user will  get from database
#playlist_id from database
#start from dummy playlist
#insert before from dumy playlist

sp.user_playlist_reorder_tracks(user, playlist_id, range_start, insert_before, range_length=1, snapshot_id=None)
