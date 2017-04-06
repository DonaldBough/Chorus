import datetime
import pprint
import sys
import os
import subprocess
import json

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
#import our classes
from database import Database
from spotify import Spotify

app = Flask(__name__)
api = Api(app)
    
class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('currentEvent', type=str)
            parser.add_argument('inEvent', type=str)
            parser.add_argument('hostID', type=str)
            args = parser.parse_args()
            
            db = Database()
            userID = db.insertUser(args['currentEvent'], args['inEvent'], args['hostID'])

            return {'userID': userID}

        except Exception as e:
            return {'error': str(e)}

class CreateHost(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('playlistID', type=str)
            parser.add_argument('spotifyToken', type=str)
            parser.add_argument('spotifyUsername', type =str)
            args = parser.parse_args()

            db = Database();
            hostID = db.insertHost(args['playlistID'], args['spotifyToken'], args['spotifyUsername']);
            return {'hostID': hostID}

        except Exception as e:
            return {'error': str(e)}

class SendVote(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('eventID', type=str)
            parser.add_argument('songID', type=int)
            args = parser.parse_args()

            db = Database();
            votes = db.isVoted(_eventID, _userID, _songID)

            if votes is not None:
                if (vote == 1 and veto == 0):
                    db.registerVote(_userID, _eventID, _songID, _vote);
                elif (vote == 0 and veto == 1):
                    db.registerVote(_userID, _eventID, _songID, _veto);
                return {'status': 'Success'} #'User ID': args['userid'], 'Event ID': args['eventid'], 'Song ID': args['songid'], 'Vote': args['vote'], 'Veto': args['veto']}
 
        except Exception as e:
            return {'error': str(e)}

class CreateEvent(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('hostID', type=int)
            parser.add_argument('explicitAllowed', type=str)
            parser.add_argument('eventName', type=str)
            parser.add_argument('accessToken', type=str)
            parser.add_argument('refreshToken', type=str)
            args = parser.parse_args()
            
            db = Database()
            db.insertEvent("LIVE", args['hostID'], args['explicitAllowed'], 
                args['eventName'], args['accessToken'], args['refreshToken'])

            eventID = db.getEventID(args['eventName'], args['hostID'])
            return {'EventID': eventID}

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

            db = Database()
            songs = db.getQueue()
            
            return {'songs': songs}

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

            db = Database()
            songs = db.getPlayedSongs(_eventID, _userID)

            return {'songs': songs}

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
            eventID = db.getEventID(_eventPassword)
            print(eventID)
            db.JoinEvent(eventID, "0", "0")



            return {'EventID': eventID}

        except Exception as e:
            return {'error': str(e)}

#define API endpoints

api.add_resource(CreateUser, '/CreateUser')
api.add_resource(CreateHost, '/CreateHost')
api.add_resource(SendVote, '/SendVote')
api.add_resource(CreateEvent, '/CreateEvent')
api.add_resource(JoinEvent, '/JoinEvent')

if __name__ == '__main__':
    app.run(debug=True)
