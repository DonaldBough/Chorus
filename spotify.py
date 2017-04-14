import requests
import spotipy
import datetime
import pprint
import sys
import os
import subprocess
import json
import spotipy.util as util
import urllib2
import time

#All functions that interact directly with the Spotify API go here

class Spotify:
    #get token
    #get current song id
    #get username
    #get track id to be played next
    #get playlist ID
    
    
    def getRecommendations(songID, token): #integrate with UI
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        db = Database()
        
        return sp.recommendations(seed_artists=None, seed_genres=None, seed_tracks={songID}, limit=15, country=US)

    def createPlaylist(username, token): #get token from database
        playlist_name = 'Chorus'
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        db = Database()
        playlists = sp.user_playlist_create(username, playlist_name)

    def addSongs(token, trackID, playlist_id): #token comes from database, trackID comes from highest voted song in database
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        #playlists = sp.user_playlists(username, limit=50, offset=0)
        # get the first album uri
        #for playlist in playlists['items']:
        #    if(playlist['name'] == "Chorus"):
        #        playlist_id = playlist['id']
        db = Database()
        sp.user_playlist_add_tracks(username, playlist_id, trackID)
        #print("playlist id: " + playlist_id)

    def authtarget(token, playlist_id, username):
    while True:
        timer(token, playlist_id, username)
        time.sleep(20)
    t = threading.Thread(target = authtarget)
    t.daemon = True
    t.start()
