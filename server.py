#forDB
import datetime
import mysql.connector
import pprint
import sys
import os
import subprocess
import spotipy
import spotipy.util as util

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)


class Spotify:

    def getUserName(self):
        return '1210281728'

    def getToken(self):
        username =  '1210281728'
        playlist_name = 'Chorus'
        scope = 'playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify'
        #put server url for redirect url
        token = util.prompt_for_user_token(username,scope,client_id='3c6df9a90b934200856b352829f09fd0',client_secret='694b8ac2f8cb478796b304fd6f1fd082',redirect_uri='http://localhost/')
        return token

    def createPlaylist(self):
        username =  '1210281728'
        playlist_name = 'Chorus'
        scope = 'playlist-read-private playlist-read-collaborative playlist-modify-private'
        #put server url for redirect url
        token = util.prompt_for_user_token(username,scope,client_id='3c6df9a90b934200856b352829f09fd0',client_secret='694b8ac2f8cb478796b304fd6f1fd082',redirect_uri='http://localhost/')
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            sp.user_playlist_create(username, playlist_name)
            # find album by name
            playlists = sp.user_playlists(username, limit=50, offset=0)

    def addSongs(self):
        username = '1210281728'
        track_ids = ["2gFvRmQiWg9fN9i74Q0aiw", "4Km5HrUvYTaSUfiSGPJeQR", "7BKLCZ1jbUBVqRi2FVlTVw", "3bi8yEuK44vLcbjHkPH0u1", "5SDVX9gpSXoE0M6KZt4EBF", "0O6jl8Zamz6TGF0nUwMQsF", "4RnfMhMUMqHlrn4V6A3KfS", "6F5c58TMEs1byxUstkzVeM", "3cfOd4CMv2snFaKAnMdnvK"]
        scope = 'playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify'
        token = util.prompt_for_user_token(username,scope,client_id='3c6df9a90b934200856b352829f09fd0',client_secret='694b8ac2f8cb478796b304fd6f1fd082',redirect_uri='http://localhost/')

        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        # find album by name
        playlists = sp.user_playlists(username, limit=50, offset=0)

        # get the first album uri
        for playlist in playlists['items']:
            if(playlist['name'] == "Chorus"):
                playlist_id = playlist['id']

        sp.user_playlist_add_tracks(username, playlist_id, track_ids)

class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('password', type=str, help='Password to create user')
            #parser.add_argument('explicit', type=bool, help='Flag to check if event exists')
            args = parser.parse_args()

            return {'Password': args['password']}

        except Exception as e:
            return {'error': str(e)}

class SendVote(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('userid', type=str, help='ID of User that is sending vote')
            parser.add_argument('eventid', type=str, help='ID of event user is in')
            parser.add_argument('songid', type=str, help='ID of song that is being voted on')
            parser.add_argument('vote', type=str, help='Email address to create user')
            parser.add_argument('veto', type=str, help='Email address to create user')
            args = parser.parse_args()

            _userID = args['userid']
            _eventID = args['eventid']
            _songID = args['songid']
            _vote = args['vote']
            _veto = args['veto']

            return {'User ID': args['userid'], 'Event ID': args['eventid'], 'Song ID': args['songid'], 'Vote': args['vote'], 'Veto': args['veto']}

        except Exception as e:
            return {'error': str(e)}

class CreateEvent(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('password', type=str, help='Password to create user')
            parser.add_argument('explicit', type=bool, help='Flag to check if event exists')
            args = parser.parse_args()

            _eventPassword = args['password']
            _eventExplicit = args['explicit']

            explicitBol = None
            if _eventExplicit: 
                explicitBol = 0
            else:
                explicitBol = 1

            db = Database()
            sp = Spotify()

            sp.createPlaylist()
            playlistID = sp.addSongs()
            print("GOT THE ID:" + playlistID)
            token = sp.getToken()
            userName = sp.getUserName()
            db.insertNewEvent("running", "2", explicitBol, _eventPassword)


            eventID = db.getEventID(_eventPassword)

            return {'EventID': eventID}

        except Exception as e:
            return {'error': str(e)}

class CreateEvent(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('password', type=str, help='Password to create user')
            parser.add_argument('explicit', type=bool, help='Flag to check if event exists')
            args = parser.parse_args()

            _eventPassword = args['password']
            _eventExplicit = args['explicit']

            explicitBol = None
            if _eventExplicit: 
                explicitBol = 0
            else:
                explicitBol = 1

            db = Database()







            db.insertNewEvent("running", "2", explicitBol, _eventPassword)


            eventID = db.getEventID(_eventPassword)

            return {'EventID': eventID}

        except Exception as e:
            return {'error': str(e)}
            
#All database functions are abstracted here
class Database:
    #cursor = None
    #cnx = None
    #Database.insertNewEvent("2", "on", "22", "yes", "dummy")
    #def __init__(self):
     #   cnx = mysql.connector.connect(user='root', password ="mynewpassword", 
      #      host="127.0.0.1", database ='mydb')
       # self.cursor = cnx.cursor(buffered = True)

    #Template for what insert statements look like, table name/columns aren't right
    def insertNewEvent(self, eventStatus, hostID, explicitAllowed, eventName):
        print("herer")
        cnx = mysql.connector.connect(user='root', password ="mynewpassword", 
            host="127.0.0.1", database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO event (eventStatus, hostID, explicitAllowed, eventName) "
            "VALUES(%s, %s, %s, %s)")
        data = (eventStatus, hostID, explicitAllowed, eventName)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def insertNewHost(self, hostID, playlistID, spotifyToken, spotifyUsername):
        cnx = mysql.connector.connect(user='root', password ="mynewpassword", 
            host="127.0.0.1", database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO host (hostID, playlistID, spotifyToken, spotifyUsername) "
           "VALUES(%s, %s, %s, %s)")
        data = (hostID, playlistID, spotifyToken, spotifyUsername)
        cursor.execute(query, data)
        #for (hostID, playlistID, spotifyToken, spotifyUsername) in cursor:
         #   print("{}, {}, {}, {}".format(
          #  hostID, playlistID, spotifyToken, spotifyUsername))
        cursor.close()
        cnx.commit()
        cnx.close()

    def getEventID(self, eventName):
        cnx = mysql.connector.connect(user='root', password ="mynewpassword", 
            host="127.0.0.1", database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT eventID FROM EVENT WHERE eventName = '" +eventName + "'")
        cursor.execute(query)
        result = cursor.fetchone()[0];
        cursor.close()
        cnx.commit()
        cnx.close()
        return result

    #for (eventID, eventStatus, hostID, explicit) in self.cursor:
    #   print("{}, {}, {}, {}".format(
    #  eventID, eventStatus, hostID, explicit))

#define API endpoints
api.add_resource(CreateUser, '/CreateUser')
api.add_resource(SendVote, '/SendVote')
api.add_resource(CreateEvent, '/CreateEvent')

if __name__ == '__main__':
    
    #db = Database()
    #db.printing()
    #db.insertNewEvent("on", "2", "0", "my")
    #result = db.getEventID("my")
    #print(result)

    app.run(debug=True)