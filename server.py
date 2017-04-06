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
            parser.add_argument('songid', type=int, help='ID of song that is being voted on')
            parser.add_argument('vote', type=str, help='Email address to create user')
            parser.add_argument('veto', type=str, help='Email address to create user')
            args = parser.parse_args()

            _userID = args['userid']
            _eventID = args['eventid']
            _songID = args['songid']
            _vote = args['vote']
            _veto = args['veto']
            
            db = Database();
            db.registerVote(_userID, _eventID, _songID, _vote, _veto);
            return {'status': 'Success'} #'User ID': args['userid'], 'Event ID': args['eventid'], 'Song ID': args['songid'], 'Vote': args['vote'], 'Veto': args['veto']}

        except Exception as e:
            return {'error': str(e)}

class CreateEvent(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('eventStatus', type=str)
            parser.add_argument('hostID', type=int)
            parser.add_argument('explicitAllowed')
            parser.add_argument('eventName', type=str)
            parser.add_argument('accessToken', type=str)
            parser.add_argument('refreshToken', type=str)
            args = parser.parse_args()
            
            db = Database()
            db.insertEvent(args['eventStatus'], args['hostID'], args['explicitAllowed'], 
                args['eventName'], args['accessToken'], args['refreshToken'])

            eventID = db.getEventID(args['eventName'], args['hostID'])
            return {'EventID': eventID}

        except Exception as e:
            return {'error': str(e)}

class getQueue(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('userid', type=str, help='ID of User that is sending vote')
            parser.add_argument('eventid', type=str, help='ID of event user is in')
            args = parser.parse_args()

            db = Database()
            return db.getQueue()

        except Exception as e:
            return {'error': str(e)}

class joinEvent(Resource):
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
            

#def insertEvent(self, eventID, eventStatus, hostID, explicit):
# newData = db.getArtistOfSong(1)
#print db.getSongID("Riptide")

# print newData

# print "Token was : %s" % db.getHostSpotifyToken(100)
#print("token was" + db.getHostSpotifyToken(100))

#define API endpoints

api.add_resource(CreateUser, '/CreateUser')
api.add_resource(SendVote, '/SendVote')
api.add_resource(CreateEvent, '/CreateEvent')
api.add_resource(joinEvent, '/JoinEvent')
if __name__ == '__main__':
    app.run(debug=True)
