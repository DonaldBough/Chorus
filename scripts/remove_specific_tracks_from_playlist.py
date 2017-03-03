
# Adds tracks to a playlist

import pprint
import sys

import spotipy
import spotipy.util as util

#once again, system call here, retrieve ids
if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    track_ids_and_positions = sys.argv[3:]
    track_ids = [ ]
    for t_pos in sys.argv[3:]:
        tid, pos = t_pos.split(',')
        track_ids.append( { "uri" : tid, "positions": [ int(pos)] } )
else:
    print("Usage: %s username playlist_id track_id,pos track_id,pos ..." % (sys.argv[0],))
    sys.exit()

#ask for token here
sp = spotipy.Spotify(auth=token)
sp.trace = False
results = sp.user_playlist_remove_specific_occurrences_of_tracks(username, playlist_id, track_ids)
pprint.pprint(results)

