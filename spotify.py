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
    playingSong
    flagFirst = True
    '''
        createPlaylist
        Def: Creates chorus playlist
        Input: username of user from database, oauth token from database
        return: playlist ID, ID of playlist created
    '''
    def createPlaylist(username, token):
        db = Database()
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
        if(flagFirst):
            playingSong = trackID
            flagFirst = False

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
        addTwo
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
    def timer(token, playlist_id, username, topVoted, songToAdd):
        #use GET command to get users played songs
        #currentSong = ""
        payload = {'limit':1}
        req = requests.get("https://api.spotify.com/v1/me/player/recently-played", data = payload, headers={"Authorization":'Bearer ' + token})
        indexID = req.text.find("id", 0, len(req.text))
        indexID = indexID + 7
        currentSong = ""

        while (req.text[indexID] != '"'):
            currentSong += req.text[indexID]
            indexID+= 1

        #debug
        #print(recentSong)

        #compare the last played track ID to trackID in server
        #if it is the different, move song ID from next to played in database
        #call query to move the song
        #change the song in server to what was played
        if (playingSong != currentSong):
            playingSong = currentSong;
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

    '''
        recommend_fallback
        Def: uses a track the user selects to add n related songs to the chorus playlist as a fallback
        Input: token, track_id from ui, num_tracks from ui possibly
        Return: N/A
    '''
    def recommend_fallback(token, track_id): 
        headers={"Authorization":'Bearer ' + token}
        count = 0
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        req = requests.get('https://api.spotify.com/v1/recommendations?seed_tracks=' + track_id, headers)
        #print(req.content)
        json_obj = json.loads(req.text)
        for i in json_obj['tracks']:
            if(count < 10):
                addSongs(token, i, playlist_id, username)
                count = count + 1

    '''
        recommend_ui
        Def: returns the json files which have recommendations based on the current track
        Input: token, tracks for what to recommend
        Returrn: req.contents, the json text
    '''
    def recommend_ui(token, tracks):
        headers={"Authorization":'Bearer ' + token}
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        req = requests.get('https://api.spotify.com/v1/recommendations?seed_tracks=' + tracks, headers={"Authorization":'Bearer ' + token})
        return req.contents

    #play playlist start
    def play(token):
        print('play')
        headers={"Authorization":'Bearer ' + token}
        requests.put('https://api.spotify.com/v1/me/player/play', headers)

    #pause playlist
    def pause(token):   
        print('pause')
        headers={"Authorization":'Bearer ' + token}
        requests.put('https://api.spotify.com/v1/me/player/pause', headers)

    #resume playlist
    def resume(token):  
        print('resume')
        headers={"Authorization":'Bearer ' + token}
        requests.put('https://api.spotify.com/v1/me/player/play', headers)

    #veto, skip track
    def skip(token):
        print('skip')
        headers={"Authorization":'Bearer ' + token}
        requests.post('https://api.spotify.com/v1/me/player/next',headers)

    #delete veto'd track from playlist
    #requests.delete('https://api.spotify.com/v1/users/%s/playlists/%s/tracks')
    def delete(token, track_id):
        print('delete')
        headers={"Authorization":'Bearer ' + token}
        sp = spotipy.Spotify(auth=token)
        sp.user_playlist_remove_all_occurrences_of_tracks(user, playlist_id, {track_id}, snapshot_id=None)
