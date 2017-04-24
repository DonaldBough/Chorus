import datetime
import pprint
import sys
import os
import subprocess
import json
import requests

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask_cors import CORS, cross_origin
#import our classes
from database import Database
from spotify import Spotify

app = Flask(__name__)
CORS(app)
api = Api(app)
    
def auth2Token(code):
    url = "https://accounts.spotify.com/api/token"
    grant_type = "authorization_code"
    #get code from UI
    redirect_uri = "http://localhost:8000/create.html"
    #redirect_uri = "http:%2F%2Flocalhost:8000%2Fcreate.html"
    client_id = "0abc049d139f4ee8b465fd9416aa358d"
    client_secret = "dd477b353e744461ae1b3062f256c952"
    payload = {'grant_type': grant_type, 'code': code, 'redirect_uri': redirect_uri, 'client_id':client_id, 'client_secret':client_secret}

    req = requests.post(url, data = payload)
    res = json.loads (req.content)

    return [res['access_token'], res['refresh_token']]

#class CreateUser(Resource):
def CreateUser(currentEvent, inEvent, isHost):
    try:
        # Parse the arguments
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('currentEvent', type=str)
        parser.add_argument('inEvent', type=str)
        parser.add_argument('host', type=str)
        args = parser.parse_args()
        '''     
        
         
        db = Database()
        userID = db.insertUser(currentEvent, inEvent, isHost)
        
        return userID
    
    except Exception as e:
        return str(e)
    
#class CreateHost(Resource):

def CreateHost(currentEvent, inEvent, isHost, spotufyUsername, playlistID, accessToken, refreshToken):
    try:
        '''
        # Parse the arguments
        parser = reqparse.RequestParser()
        parser.add_argument('playlistID', type=str)
        parser.add_argument('spotifyToken', type=str)
        parser.add_argument('spotifyUsername', type =str)
        args = parser.parse_args()
        '''
        db = Database()
        hostID = db.insertHost(currentEvent, inEvent, isHost, spotufyUsername, playlistID, accessToken, refreshToken)
        return hostID
    
    except Exception as e:
        return {'error': str(e)}

class SendVote(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('userID', type=int)
            parser.add_argument('eventID', type=int)
            parser.add_argument('songID', type=str)
            parser.add_argument('vote', type=int)
            parser.add_argument('veto', type=int)
            args = parser.parse_args()
            
            _userID = args['userID']
            _eventID = args['eventID']
            _songID = args['songID']
            _vote = args['vote']
            _veto = args['veto']

            db = Database();
            votes = db.isVoted(_eventID, _userID, _songID)

            if (votes == -1):
                if (_vote == 1 and _veto == 0):
                    db.registerVote(_songID)
                    db.updateVote(_userID, _eventID, _songID, _vote)
                    return {'status': 'Success'}
                elif (_vote == 0 and _veto == 1):
                    db.registerVeto(_songID)
                    db.updateVeto(_userID, _eventID, _songID, _veto)
                    return {'status': 'Success'} #'User ID': args['userid'], 'Event ID': args['eventid'], 'Song ID': args['songid'], 'Vote': args['vote'], 'Veto': args['veto']}
            return {'status': 'Failure'}

        except Exception as e:
            return {'error': str(e)}

class CreateEvent(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('explicitAllowed', type=str)
            parser.add_argument('eventName', type=str)
            parser.add_argument('authCode', type=str)
            args = parser.parse_args()
            _authCode    = args['authCode']
            tokens       = auth2Token(_authCode)
            print(tokens)
            accessToken  = tokens[0]
            refreshToken = tokens[1]
            print("here0")
            sp  = Spotify()
            ids = sp.createPlaylist(accessToken)
            print("here1")
            print(ids[0])
            print(ids[1])
            hostID = CreateHost("0", "0", "1", ids[0], ids[1], accessToken, refreshToken) #######username, playlistid
            db     = Database()
            print(hostID)
            db.insertEvent("LIVE", hostID, args['explicitAllowed'], 
                           args['eventName'])
            print("here2")
            eventID = db.getEventid(args['eventName'])
            db.updateHostEventID(hostID, eventID)
            print("here3")
            sp.addTwo(eventID)
            print("here4")
            sp.play(eventID)
            print("here5")
            #sp.authtarget(hostID)
            #print("here6")

            return json.dumps({'eventID': eventID, 'hostID': hostID})

        except Exception as e:
            return {'error': str(e)}

class GetQueue(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('userid', type=str, help='ID of User that is sending vote')
            parser.add_argument('eventid', type=str, help='ID of event user is in')
            args = parser.parse_args()

            _userID = args['userid']
            _eventID = args['eventid']

            db = Database()
            songs = db.getQueue(_eventID, _userID)

            return json.dumps({'songs': songs})

        except Exception as e:
            return {'error': str(e)}

class GetPlayedSongs(Resource):
    def post(self):
        try:
            # Parse the arguments                                                                                               
            parser = reqparse.RequestParser()
            parser.add_argument('userid', type=str, help='ID of User that is sending vote')
            parser.add_argument('eventid', type=str, help='ID of event user is in')
            args = parser.parse_args()

            _userID = args['userid']           
            _eventID = args['eventid']

            db = Database()
            print(_eventID)
            print(_userID)
            songs = db.getPlayedSongs(_eventID, _userID)

            return json.dumps({'songs': songs})

        except Exception as e:
            return {'error': str(e)}

class JoinEvent(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _eventPassword = args['password']
    
            #print(_eventPassword)
            db = Database()
            #print("name :" +_eventPassword)
            
            eventID = db.getEventid(_eventPassword)
            userID  = CreateUser(eventID, "0", "0")
            
            return json.dumps({'eventID': eventID, 'userID': userID})

        except Exception as e:
            return {'error': str(e)}

class JoinSpotify(Resource): #############
    def post(self):
        try:
            # Parse the arguments                                                                                                  
            parser = reqparse.RequestParser()
            parser.add_argument('authCode', type=str)
            parser.add_argument('userID', type=str)
            args = parser.parse_args()

            _authCode    = args['authCode']
            _userID      = args['userID']
            tokens       = auth2Token(_authCode)
            accessToken  = tokens[0]
            refreshToken = tokens[1]

            sp         = Spotify()
            username   = sp.guestUsername(accessToken)
            playlistID = sp.createGuestPlaylsit(userID) ##########
            
            db = Database()
            db.insertUserData(userID, username, acessToken) ##########
            db.insertPlaylistID(userID, playlistID) ########

        except Exception as e:
            return {'error': str(e)}

'''
class CreateGuestPlaylist(Resource): #################
    def post(self):
        try:
            # Parse the arguments                                                                                                         
            parser = reqparse.RequestParser()
            parser.add_argument('userID', type=str)

            userID  = args['userID']

            sp = Spotify()
            playlistID = sp.createGuestPlaylsit(userID)

            db = Database()
            db.insertPlaylistID
            return {status : 'Success'}

        except Exception as e:
            return {'error': str(e)}
'''
'''
class GuestAdd(Resoruce): #################
    def post(self):
        try:
            # Parse the arguments                                                                                               
            parser = reqparse.RequestParser()
            parser.add_argument('userID', type=str)
            parser.add_argument('songID', type=str)

            userID = args['userID']
            songID = args['songID']

            sp = Spotify()
            sp.guestAdd(userID, songID)

            return {status : 'Success'}

        except Exception as e:
            return {'error': str(e)}

class Search(Resource): ##################
    def post(self):
        try:
            # Parse the arguments                                                                                                           
            parser = reqparse.RequestParser()
            parser.add_argument('query', type=str)
            
            query = args['query']
            sp = Spotify()
            results = sp.search(query)

            return {'results': results}

        except Exception as e:
            return {'error': str(e)}
'''

#define API endpoints
#api.add_resource(CreateUser, '/CreateUser')
#api.add_resource(CreateHost, '/CreateHost')
api.add_resource(SendVote, '/SendVote')
api.add_resource(CreateEvent, '/CreateEvent')
api.add_resource(JoinEvent, '/JoinEvent')
api.add_resource(GetQueue, '/GetQueue')
api.add_resource(GetPlayedSongs, '/GetPlayedSongs')

if __name__ == '__main__':
    app.run(debug=True)
