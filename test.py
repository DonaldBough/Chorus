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

'''
    createPlaylist
    Def: Creates chorus playlist
    Input: username of user from database, oauth token from database
    return: playlist ID, ID of playlist created
'''
def createPlaylist(username, token):
    playlist_name = 'Chorus'
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    sp.user_playlist_create(username, playlist_name)
    playlists = sp.user_playlists(username, limit=50, offset=0)
    
    for playlist in playlists['items']:
        if(playlist['name'] == "Chorus"):
            playlist_id = playlist['id']
            
    return playlist_id

'''
    addSongs
    Def: Adds song to chorus playlist
    Input: oauth token from database, trackID from what user requests (UI), playlist_id from database/ other functions, username from database/other function
    return: N/A
'''
def addSongs(token, trackID, playlist_id, username):
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    sp.user_playlist_add_tracks(username, playlist_id, trackID)

'''
    hostUserId
    Def: Adds song to chorus playlist
    Input: oauth token from database
    return: userID, current user's ID
'''
def hostUserId(token):
    #use GET command to get user info
    req = requests.get("https://api.spotify.com/v1/me", headers={"Authorization":'Bearer ' + token})
    #gets start of user id
    indexID = req.text.find("id", 0, len(req.text))
    indexID = indexID + 7
    userID = ""
    
    while (req.text[indexID] != '"'):
        userID += req.text[indexID]
        indexID+= 1
        
    return userID

'''
    addSongs
    Def: Adds song to chorus playlist
    Input: oauth token from database, trackID from what user requests (UI), playlist_id from database/ other functions, username from database/other function
    return: N/A
'''   
def addTwo(token, username, playlist_id):
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    sp.user_playlist_add_tracks(username, playlist_id, {'7qiZfU4dY1lWllzX7mPBI3', '0KKkJNfGyhkQ5aFogxQAPU'})

'''
    addSongs
    Def: Adds top voted song to playlist if there is no longer a locked in song
    Input: oauth token from database, playlist_id from database/ other functions, trackID from what user requests (UI),
    username from database/other function, currentSong from server, topVoted from database
    return: N/A
'''
def timer(token, playlist_id, username, currentSong, topVoted):
    #use GET command to get users played songs
    payload = {'limit':1}
    req = requests.get("https://api.spotify.com/v1/me/player/recently-played", data = payload, headers={"Authorization":'Bearer ' + token})
    indexID = req.text.find("id", 0, len(req.text))
    indexID = indexID + 7
    recentSong = ""
    
    while (req.text[indexID] != '"'):
        recentSong += req.text[indexID]
        indexID+= 1

    #debug
    #print(recentSong)
    
    #compare the last played track ID to trackID in server
    #if it is the different, move song ID from next to played in database
    #call query to move the song
    #change the song in server to what was played
    if (currentSong != recentSong):
        currentSong = recentSong;
        addSongs(token, {songToAdd}, playlist_id, username)
        print("song added")
    
    #do nothing if it is the same   
    else:
        print "the same"

'''
    authtarget
    Def: Runs timer function every 30 seconds to lock in the top voted song on a different thread
    Input: oauth token from database, playlist_id from database/ other functions, trackID from what user requests (UI),
    username from database/other function, currentSong from server, topVoted from database
    return: N/A
'''
def authtarget(token, playlist_id, username, currentSong, topVoted):
    while True:
        timer(token, playlist_id, username, currentSong, topVoted)
        time.sleep(30)
    t = threading.Thread(target = authtarget)
    t.daemon = True
    t.start()
    #do we need to put raw_input for the rest of the stuff?


if __name__ == '__main__':
    token = 'BQByLERbVV1anMC_MRq9K4FLOy7rFC8qFNA6qqLUPNVGt5h-_Lvj-TxSNLcnmyxlcsYMB7lg4NnzQZMS_fMEQrfgtOMqfILwyRPxLSAtx2fhn4oW6CzBQo6_i2GNNlY4mTO2_jKnj3juEjtqIjNg7TYwvkP-hu3mT9vHlBbg61GgWsydoaWLZ6k7omQ41haj6qYuZN6nOFHPRX7UGDwiUQaHmnrfIvz6i2ybBPq0jNOTP6yJDEoCWGPvo8ZJPkFqIrl4aUCVig73_5j19STk_ArMCsE1EE7WyOjz3IqZVjjSDuiic-P1y1SxnFdU_I95kWk'
    currentSong = '3AA28KZvwAUcZuOKwyblJQ'
    topVoted = '7qiZfU4dY1lWllzX7mPBI3'
    username = hostUserId(token)
    playlist_id = createPlaylist(username, token)
    addTwo(token, username, playlist_id)
    authtarget(token, playlist_id, username, currentSong, topVoted)
    
    
    
