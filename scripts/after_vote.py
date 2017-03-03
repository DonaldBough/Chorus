import pprint
import sys

import spotipy
import spotipy.util as util

#server call instead of sys.argv
if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    range_start =
    range_length =
    insert_before =
    snapshot_id =
    
else:
    print "Usage: %s username playlist_id track_id ..." % (sys.argv[0],)
    sys.exit()

#get token from database

sp = spotipy.Spotify(auth=token)
sp.trace = False
sp.user_playlist_reorder_tracks(user, playlist_id, range_start, insert_before, range_length=1, snapshot_id=None)

  
