import pprint
import sys
import spotipy
import spotipy.util as util

#get refreshtoken from stored in database

sp = spotipy.Spotify(auth=token)
sp.trace = False
sp.refresh_access_token(refresh_token)
