import pprint
import sys
import spotipy
import spotipy.util as util

#get the song playing's artist, the song itself as the track, genres from the song
sp = spotipy.Spotify(auth=token)
sp.trace = False

return sp.recommendations(seed_artists=None, seed_genres=sp.recommendation_genre_seeds(), seed_tracks=None, limit=50, country=US, **kwargs)
