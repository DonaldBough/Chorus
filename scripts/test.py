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
import time;

def createPlaylist(username, token): #get token from database
    playlist_name = 'Chorus'
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    sp.user_playlist_create(username, playlist_name)
    playlists = sp.user_playlists(username, limit=50, offset=0)
    for playlist in playlists['items']:
        if(playlist['name'] == "Chorus"):
            playlist_id = playlist['id']
                
    return playlist_id

def addSongs(token, trackID, playlist_id, username): #token comes from database, trackID comes from highest voted song in database
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    #playlists = sp.user_playlists(username, limit=50, offset=0)
    # get the first album uri
    #for playlist in playlists['items']:
    #    if(playlist['name'] == "Chorus"):
    #        playlist_id = playlist['id']
    sp.user_playlist_add_tracks(username, playlist_id, trackID)
    #print("playlist id: " + playlist_id)

def hostUserId():
    #use GET command to get users info
    params = {"limit":1}
    responsestring = requests.get("https://api.spotify.com/v1/me", headers={"Authorization":token})
                                  #params, headers={"Authorization":token})
    #Find index make the hostID string
    print(responsestring.content)
    indexID = str.find("\"id\":", 0, len(responsestring.json()))
    indexID = indexID + 6
    s = ""
    while (responsestring[indexID] != '"'):
        s += responsestring[indexID]
        indexID+= 1
    #s will equal hostUSERID
    return s
    #currentSong = 'Start'
    #recentSong = 'recent'

def addTwo(token, username, playlist_id):
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    sp.user_playlist_add_tracks(username, playlist_id, {'7qiZfU4dY1lWllzX7mPBI3', '0KKkJNfGyhkQ5aFogxQAPU'})

def timer(token, playlist_id, username):
    #use GET command to get users played songs
    #GET https://a.spotify.com/v1/me/player/recently-played #change up some things still
    #find the index and make the string
    #req = requests.get("https://api.spotify.com/v1/me/player/recently-played", data = {'limit': 1}, headers={"Authorization": token})
    #print(req.text) 
    #indexID = str.find("\"id\":", 0, len(req.text))
    #indexID = indexID + 6
    #recentSong = req[indexID: indexID+22]
    #compare the last played track ID to trackID in server
    #if (currentSong != recentSong):
    #if it is the different, move song ID from next to played in database
    #call query to move the song
    #change the song in server to what was played
        #currentSong = recentSong;
        #then call addSong, which adds the top voted song into the playlist
        #call top song in database
        #top_song = 
    addSongs(token, {'7qiZfU4dY1lWllzX7mPBI3'}, playlist_id, username)
    print("song added")
    
    #if it is the same, then chill   
    #print "the same"

def authtarget(token, playlist_id, username):
    while True:
        timer(token, playlist_id, username)
        time.sleep(20)
    t = threading.Thread(target = authtarget)
    t.daemon = True
    t.start()
    #do we need to put raw_input for the rest of the stuff?


if __name__ == '__main__':
    #username = hostUserId()
    username = '1237666383'
    token = 'BQCFVPR1Q68vFRjM-yE6ScSioD2A_RpTfoWoPWxXTSeMbNenMi932ihODVLmLQ3fZTpfiHairxSsf_ipcnBXiB1ayajzIHTUu8agM8BNh09dRg7Ym5g24465_aI9Wu07Hlxp5cdgra432XTQcS21ziZPCC214T3TaPSIk2FnNUf-j_Ab37hnJYq14lem689P476Tj2CM6fuUo_yTQ0XmdTaeAfIrr2kpQpBQBtaria0zKiZ-6drl7cC6UWH3rIVggHKOZpycT6oK3y8'
    playlist_id = createPlaylist(username, token)
    addTwo(token, username, playlist_id)
    timer(token, playlist_id, username)
    authtarget(token, playlist_id, username)
    
    
    
