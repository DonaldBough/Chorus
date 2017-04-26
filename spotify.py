
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

globalToken = "BQCrhgmICeTIG6eUh0XhB5W6ywUQhibY-se4YIuBfXHW7jb5BSn3-_bKvZVKACNYMULg1UgwFndQp4gtFMTWw5uYqECpJg30z-z3hv9dz9NZ2BpPSsZq_gxFlZsmJ6RoJoEQOw1fJluvJkgl6MrQDpk7HnxcIH0uoWbOZgwUERI6HAjh6cms0ozPJFB87WXnUvwTV-vKx9zFODvbARDa3wA3Gyu6nB7YHt958f3mamNPf9Ukqq5V7uaXaDh5Nfe58Cg7yjX1tF-7s2A4M_WtImjH9IlakKrT_tAWL9rNabTSkSSRFpPmg_0GUc6gx-w"

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
    def search(self, name):
        sp = spotipy.Spotify()
        sp.trace = False
        results = spotify.search(q='artist:' + name, type='track')
        return results
    
    def createPlaylist(self, token):
        #db = Database()
        #token = db.getEventSpotifyToken(eventID)
        #use GET command to get user info
        req = requests.get("https://api.spotify.com/v1/me", headers={"Authorization":'Bearer ' + token})
        j = json.loads(req.text)
        userID = j['id'] 
        #print("userID === " + userID)
        playlist_name = 'Chorus'
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        sp.user_playlist_create(userID, playlist_name)
        playlists = sp.user_playlists(userID, limit=50, offset=0)

        for playlist in playlists['items']:
            if(playlist['name'] == "Chorus"):
                playlist_id = playlist['id']
        
        headers={"Authorization":'Bearer ' + token}
        requests.put('https://api.spotify.com/v1/me/player/shuffle?state=false',headers={"Authorization":'Bearer ' + token})
        
        data = []
        data.append(userID)
        data.append(playlist_id)
        return data
    
    def getPlaylistUrl(self, eventID):
        db = Database()
        userID = db.getHostSpotifyUserName(eventID)
        playlist_id = db.getPlaylistID(eventID)
        url = ('https://open.spotify.com/user/' + userID + '/playlist/' + platlist_id)
        return url
    
    def addSongs(self, eventID):
        db = Database()
        trackID = db.getTopSong(eventID)
        token = globalToken#"BQBn6fdfTF3D0kQ8hMUVik1AyZES2izfbHj8btVjmY_WUAFxUwdsJUMjuONjyyc2kP6YF1d324MLl3enBjElWLeWOB2hyYgnERptowErXHFLiEg3K1wEMe-85g1wQEdt9U1QnoRbPh8US-dR7Qajt9GnHSdIoZ7Ie47BvmKefGPEocsVdhk_jHv1JEoPdzST5lMg_3gZqu_8j3E_gYtn-4aCdQxRlTxfu43EYxqKIZSDe8FYZMHmvaMUkIwr6wKnqvAjOgxuyP82bnoYeHhFQMyVQqZr_WMrGDo_d7Z8s3u6Ir1VLyUSSx5qOxLAA-SP_A"
        username = db.getHostSpotifyUserName(eventID)
        playlist_id = db.getPlaylistID(eventID)
        if(trackID == -1): print("NO TOP VOTED")
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        print("100%")
        sp.user_playlist_add_tracks(username, str(playlist_id), {str(trackID)})
        print("NOT 100%")

    def guestUsername(self, token):
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

    
    def addTwo(self, eventID):
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        username = db.getHostSpotifyUserName(eventID)
        playlist_id = db.getPlaylistID(eventID)
        #print("--------")
        #print(username)
        #print(playlist_id)
        #print("--------")
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        #ERROR: int has no attribute split
        sp.user_playlist_add_tracks(username, str(playlist_id), {'0KKkJNfGyhkQ5aFogxQAPU', '6b8Be6ljOzmkOmFslEb23P'})
        #, '0KKkJNfGyhkQ5aFogxQAPU'
        db.updateCurrentSong('0KKkJNfGyhkQ5aFogxQAPU', eventID)
        db.insertSong('0KKkJNfGyhkQ5aFogxQAPU', eventID, "0", "Thats What I Like", "Bruno Mars", "0", "0", "0")
        db.insertSong('6b8Be6ljOzmkOmFslEb23P', eventID, "0", "24K Magic", "Bruno Mars", "0", "0", "0")

    def addFive(self, eventID):
        db = Database()
        #db.insertSong('6b8Be6ljOzmkOmFslEb23P', eventID, "0",  "24K Magic", "Bruno Mars", "0", "0", "0")
        db.insertSong('0mBKv9DkYfQHjdMcw2jdyI', eventID, "0",  "Chunky", "Bruno Mars", "0", "0", "0")
        #db.insertSong('0KKkJNfGyhkQ5aFogxQAPU', eventID, "0",  "That's What I Like", "Bruno Mars", "0", "0", "0")
        db.insertSong('0kN8xEmgMW9mh7UmDYHlJP', eventID, "0",  "Straight Up & Down", "Bruno Mars", "0", "0", "0")
        db.insertSong('5XMkENs3GfeRza8MfVAhjK', eventID, "0",  "Finesse", "Bruno Mars", "0", "0", "0")
        
    def createGuestPlaylist(self, userID):
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
    
    def guestAdd(self, userID, songID):
        db = Database()
        playlist_id = db.getPlaylist(userID)
        token = db.getGuestSpotifyToken(userID)
        sp = spotipy.Spotify(auth=token)
        sp.trace = False              
        sp.user_playlist_add_tracks(userID, playlist_id, songID)
    '''        
    def timer(self, eventID):
        #use GET command to get users played songs
        #currentSong = ""
        #print "bye"
        db = Database()
        token = "BQDY-LLv98Sw21oGLdgAyJZPm-zX4stEjvbXylYED-a3ethyaov6wIK7ltX_9aN4Xs1E43yv2UwzldVoaoZ5f4E6v7Y1GWcrAj2WrOHdyqTMVHi9RbVXgUXRNgycS6tjws89QH-z-yQ0Mz0bO_DJHIuHpgbiPQfd2AYh49TcMF2oimtpac8NcFJfLCOKr4hzGr3sz5z2fr0PsHh8JiivpOy0PheM0uDfXdBhEwOqoheM8PmhWCgRU0dA1ZZaBTAWUbpzxAXmCk1PNiuyU721uXiHT5PJzxRBr_C8-VXkWnlsPcqjRRUjdOYvNZB30w"#db.getGuestSpotifyToken(userID)
        playingSong = db.getCurrentPlayingSong(eventID)
        req = requests.get("https://api.spotify.com/v1/me/player/recently-played", headers={"Authorization":'Bearer ' + token})
        #indexID = req.text.find("id", 0, len(req.text))
        #indexID = indexID + 7
        #currentSong = ""
        j = json.loads(req.text)
        currentSong = j['id'] 
        #while (req.text[indexID] != '"'):
         #   currentSong += req.text[indexID]
          #  indexID+= 1
        #compare the last played track ID to trackID in server
        #if it is the different, move song ID from next to played in database
        #call query to move the song
        #change the song in server to what was played
        if (playingSong != currentSong):
            playingSong = currentSong;
            db.updateCurrentSong(playingSong, eventID)
            #send playingSong back to db
            addSongs(eventID)
            print("song added")
            
        #do nothing if it is the same   
        else:
            print "the same"
    '''

    def timer(self, eventID):
        #print("timer")
        db = Database()
        sp  = Spotify()
        token = globalToken#"BQBn6fdfTF3D0kQ8hMUVik1AyZES2izfbHj8btVjmY_WUAFxUwdsJUMjuONjyyc2kP6YF1d324MLl3enBjElWLeWOB2hyYgnERptowErXHFLiEg3K1wEMe-85g1wQEdt9U1QnoRbPh8US-dR7Qajt9GnHSdIoZ7Ie47BvmKefGPEocsVdhk_jHv1JEoPdzST5lMg_3gZqu_8j3E_gYtn-4aCdQxRlTxfu43EYxqKIZSDe8FYZMHmvaMUkIwr6wKnqvAjOgxuyP82bnoYeHhFQMyVQqZr_WMrGDo_d7Z8s3u6Ir1VLyUSSx5qOxLAA-SP_A"
        if((str(token)  != '-1')):
            if((str(token)  != 'None')):
                try:
                    playingSong = db.getCurrentPlayingSong(eventID)
                    #req = requests.get("https://api.spotify.com/v1/me/player/recently-played", headers={"Authorization":'Bearer ' + str(token)})
                    req = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers={"Authorization":'Bearer ' + str(token)}) 
                    #print(req.text)
                    j = json.loads(req.text)
                    currentSong = j['item']['id']
                    print(playingSong)
                    print(currentSong)
                    if (playingSong != currentSong and playingSong != -1):
                        print("ENTERED IF STATEMENT")
                        db.transfer(playingSong)
                        db.deleteVoteSong(playingSong, eventID)
                        db.deleteNextSong(playingSong, eventID)
                        playingSong = currentSong;
                        db.updateCurrentSong(playingSong, eventID)
                        print 'going to add song'
                        sp.addSongs(eventID)
                        print("song added")
                        
                    else:
                        print "the same"
                except:
                    print 'invalid token'
    '''
    authtarget
    Def: Runs timer function every 30 seconds to lock in the top voted song on a different thread
    Input: oauth token from database, playlist_id from database/ other functions, trackID from what user requests (UI),
    username from database/other function, currentSong from server, topVoted from database
    return: N/A
    
    def authtarget(self):
        db = Database()
        resultList = []
        while True:
            resultList = db.getAllEventID()
            time.sleep(5)
            for i in resultList: self.timer(i) 
        t = threading.Thread(target = authtarget)
        t.daemon = True
        t.start()
        #do we need to put raw_input for the rest of the stuff?

    
        recommend_fallback
        Def: uses a track the user selects to add n related songs to the chorus playlist as a fallback
        Input: token, track_id from ui, num_tracks from ui possibly
        Return: N/A
    '''
    def recommend_fallback(self, eventID): 
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
            if(count < 1):
                addSongs(token, i, playlist_id, username)
                count = count + 1
            break

    '''
        recommend_ui
        Def: returns the json files which have recommendations based on the current track
        Input: token, tracks for what to recommend
        Returrn: req.contents, the json text
    '''
    def recommend_ui(self, eventID):
        db = Database()
        token = db.getEventSpotiyToken(eventID)
        headers={"Authorization":'Bearer ' + token}
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        req = requests.get('https://api.spotify.com/v1/recommendations?seed_tracks=' + tracks, headers={"Authorization":'Bearer ' + token})
        return req.contents

    def start(self, eventID):
        db = Database()
        token = globalToken#"BQBn6fdfTF3D0kQ8hMUVik1AyZES2izfbHj8btVjmY_WUAFxUwdsJUMjuONjyyc2kP6YF1d324MLl3enBjElWLeWOB2hyYgnERptowErXHFLiEg3K1wEMe-85g1wQEdt9U1QnoRbPh8US-dR7Qajt9GnHSdIoZ7Ie47BvmKefGPEocsVdhk_jHv1JEoPdzST5lMg_3gZqu_8j3E_gYtn-4aCdQxRlTxfu43EYxqKIZSDe8FYZMHmvaMUkIwr6wKnqvAjOgxuyP82bnoYeHhFQMyVQqZr_WMrGDo_d7Z8s3u6Ir1VLyUSSx5qOxLAA-SP_A"
#db.getEventSpotiyToken(eventID)
        hostID = db.getHostSpotifyUserName(eventID)
        print(hostID)
        playlistID = db.getPlaylistID(eventID)
        url = 'spotify:user:' + str(hostID) + ':playlist:' + str(playlistID)
        payload = {"context_uri": url}
        print("URL = " + url)
        r = requests.put('https://api.spotify.com/v1/me/player/play', data=json.dumps(payload), headers={"Accept": "application/json", "Authorization":'Bearer ' + str(token)})
        r = requests.put('https://api.spotify.com/v1/me/player/volume=?volume_percent=50', headers={"Accept": "application/json", "Authorization":'Bearer ' + str(token)})
        print(r.content)

    #play playlist start
    def play(self, eventID):
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        #print('play')
        headers={"Authorization":'Bearer ' + str(token)}
        requests.put('https://api.spotify.com/v1/me/player/play', headers={"Authorization":'Bearer ' + str(token)})

    #pause playlist
    def pause(self, eventID):
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        #print('pause')
        headers={"Authorization":'Bearer ' + token}
        requests.put('https://api.spotify.com/v1/me/player/pause', headers={"Authorization":'Bearer ' + token})

    #resume playlist
    def resume(self, eventID):  
        #print('resume')
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        headers={"Authorization":'Bearer ' + token}
        requests.put('https://api.spotify.com/v1/me/player/play', headers={"Authorization":'Bearer ' + token})

    #veto, skip track
    def skip(self, eventID):
        #print('skip')
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        headers={"Authorization":'Bearer ' + token}
        requests.post('https://api.spotify.com/v1/me/player/next',headers={"Authorization":'Bearer ' + token})
    #delete veto'd track from playlist
    #requests.delete('https://api.spotify.com/v1/users/%s/playlists/%s/tracks')
    def deleteSong(self, eventID):
        #print('delete')
        db = Database()
        token = db.getEventSpotifyToken(eventID)
        user = db.getHostID(eventID)
        playlist_id = db.getPlaylistID(eventID)
        headers={"Authorization":'Bearer ' + token}
        sp = spotipy.Spotify(auth=token)
        sp.user_playlist_remove_all_occurrences_of_tracks(user, playlist_id, {track_id}, snapshot_id=None)
