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
from database import Database

#All functions that interact directly with the Spotify API go here

class Spotify:
    #get token
    #get current song id
    #get username
    #get track id to be played next
    #get playlist ID
    
    '''
        authorize
        Input: code
        return: text that has the authorization
    
    def authorize(code):
        url = "https://accounts.spotify.com/api/token"
        grant_type = "authorization_code"
        redirect_uri = "http://localhost:8000/create.html"
        client_id = "0abc049d139f4ee8b465fd9416aa358d"
        client_secret = "dd477b353e744461ae1b3062f256c952"
        payload = {'grant_type': grant_type, 'code': code, 'redirect_uri': redirect_uri, 'client_id':client_id, 'client_secret':client_secret}
        req = requests.post(url, data = payload)
        return req.content
    '''
    
    '''
        createPlaylist
        Def: Creates chorus playlist
        Input: username of user from database, oauth token from database
        return: playlist ID, ID of playlist created
    '''
    def search(name)
        sp = spotipy.Spotify()
        sp.trace = False
        results = spotify.search(q='artist:' + name, type='track')
        return results
    
    def createPlaylist(token):
        #db = Database()
        #token = db.getEventSpotifyToken(eventID)
        #use GET command to get user info
        req = requests.get("https://api.spotify.com/v1/me", headers={"Authorization":'Bearer ' + token})
        #gets start of user id
        indexID = req.text.find("id", 0, len(req.text))
        indexID = indexID + 7
        userID = ""

        while (req.text[indexID] != '"'):
            userID += req.text[indexID]
            indexID+= 1
            
        playlist_name = 'Chorus'
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        sp.user_playlist_create(userID, playlist_name)
        playlists = sp.user_playlists(userID, limit=50, offset=0)

        for playlist in playlists['items']:
            if(playlist['name'] == "Chorus"):
                playlist_id = playlist['id']
        
        data = []
        data.append(userID)
        data.append(playlist_id)
        return data
    
    def getPlaylistUrl(eventID)
        db = Database()
        userID = db.getHostSpotifyUserName(eventID)
        playlist_id = db.getPlaylistID(eventID)
        url = ('https://open.spotify.com/user/' + userID + '/playlist/' + platlist_id)
        return url
    
    def addSongs(eventID):
        db = Database()
        trackID = db.getTopSong(eventID)
        token = db.getEventSpotifyToken(eventID)
        username = db.getHostSpotifyUserName(eventID)
        playlist_id = db.getPlaylistID(eventID)
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        sp.user_playlist_add_tracks(username, playlist_id, trackID)


    def guestUsername(token):
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

    
    def addTwo(eventID):
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        username = db.getHostSpotifyUserName(eventID)
        playlist_id = db.getPlaylistID(eventID)
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        sp.user_playlist_add_tracks(username, playlist_id, {'7qiZfU4dY1lWllzX7mPBI3', '0KKkJNfGyhkQ5aFogxQAPU'})
        db.updateCurrentSong('7qiZfU4dY1lWllzX7mPBI3', eventID)

        
    def createGuestPlaylist(userID):
        #db = Database()
        #token = db.getEventSpotifyToken(eventID)
        #use GET command to get user info
        #req = requests.get("https://api.spotify.com/v1/me", headers={"Authorization":'Bearer ' + token})
        #gets start of user id
        #indexID = req.text.find("id", 0, len(req.text))
        #indexID = indexID + 7
        #userID = ""

        #while (req.text[indexID] != '"'):
        #    userID += req.text[indexID]
        #    indexID+= 1
            
        playlist_name = 'Chorus'
        token = db.getUserToken(userID)
        username = db.getGuestUsername(userID)
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        sp.user_playlist_create(username, playlist_name)
        playlists = sp.user_playlists(userID, limit=50, offset=0)
        
        for playlist in playlists['items']:
            if(playlist['name'] == "Chorus"):
                playlist_id = playlist['id']
        return playlist_id
        
    '''
        addSongs
        Def: Adds top voted song to playlist if there is no longer a locked in song
        Input: oauth token from database, playlist_id from database/ other functions, trackID from what user requests (UI),
        username from database/other function, currentSong from server, topVoted from database
        return: N/A
    '''
    
    def guestAdd(userID, songID):
        db = Database()
        playlist_id = db.getPlaylist(userID)
        token = db.getGuestSpotifyToken(userID)
        sp = spotipy.Spotify(auth=token)
        sp.trace = False              
        sp.user_playlist_add_tracks(userID, playlist_id, songID)
        
    def timer(eventID):
        #use GET command to get users played songs
        #currentSong = ""
        db = Database()
        token = db.getGuestSpotifyToken(userID)
        playingSong = db.getCurrentPlayingSong(eventID)
        req = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers={"Authorization":'Bearer ' + token})
        indexID = req.text.find("id", 0, len(req.text))
        indexID = indexID + 7
        currentSong = ""

        while (req.text[indexID] != '"'):
            currentSong += req.text[indexID]
            indexID+= 1
        #compare the last played track ID to trackID in server
        #if it is the different, move song ID from next to played in database
        #call query to move the song
        #change the song in server to what was played
        if (playingSong != currentSong):
            playingSong = currentSong;
            db.updateCurrentSong(playingSong, eventID)
            #send playingSong back to db
            #addSongs(eventID)
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
    def authtarget():
        db = Database()
        resultList = []
        while True:
            resultList = db.getAllEventID()
            time.sleep(30)
            for i in resultList: timer(i) 
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
    def recommend_fallback(eventID): 
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        playlist_id = db.getPlaylistID(eventID)
        username = db.getHostID(eventID)
        track_id = db.getCurrentPlayingSong(eventID)
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
    def recommend_ui(eventID):
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        headers={"Authorization":'Bearer ' + token}
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        req = requests.get('https://api.spotify.com/v1/recommendations?seed_tracks=' + tracks, headers={"Authorization":'Bearer ' + token})
        return req.contents

    #play playlist start
    def play(eventID):
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        #print('play')
        headers={"Authorization":'Bearer ' + token}
        requests.put('https://api.spotify.com/v1/me/player/play', headers={"Authorization":'Bearer ' + token})

    #pause playlist
    def pause(eventID):
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        #print('pause')
        headers={"Authorization":'Bearer ' + token}
        requests.put('https://api.spotify.com/v1/me/player/pause', headers={"Authorization":'Bearer ' + token})

    #resume playlist
    def resume(eventID):  
        #print('resume')
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        headers={"Authorization":'Bearer ' + token}
        requests.put('https://api.spotify.com/v1/me/player/play', headers={"Authorization":'Bearer ' + token})

    #veto, skip track
    def skip(eventID):
        #print('skip')
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        headers={"Authorization":'Bearer ' + token}
        requests.post('https://api.spotify.com/v1/me/player/next',headers={"Authorization":'Bearer ' + token})

    #delete veto'd track from playlist
    #requests.delete('https://api.spotify.com/v1/users/%s/playlists/%s/tracks')
    def deleteSong(eventID):
        #print('delete')
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        user = db.getHostID(eventID)
        playlist_id = db.getPlaylistID(eventID)
        headers={"Authorization":'Bearer ' + token}
        sp = spotipy.Spotify(auth=token)
        sp.user_playlist_remove_all_occurrences_of_tracks(user, playlist_id, {track_id}, snapshot_id=None)
