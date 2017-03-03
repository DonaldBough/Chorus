#forDB
import datetime
import mysql.connector

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = args['password']

            return {'Email': args['email'], 'Password': args['password']}

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
    def insertNewEvent(self, eventId, eventStatus, hostID, explicitAllowed, eventName):
        cnx = mysql.connector.connect(user='root', password ="mynewpassword", 
            host="127.0.0.1", database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO event (eventId, eventStatus, hostID, explicitAllowed, eventName) "
            "VALUES(%s, %s, %s, %s, %s)")
        data = (eventId, eventStatus, hostID, explicitAllowed, eventName)
        cursor.execute(query, data)
        cursor.close()
        cnx.close()
        #self.cursor.commit

    def insertNewHost(self, hostID, playlistID, spotifyToken, spotifyUsername):
        cnx = mysql.connector.connect(user='root', password ="mynewpassword", 
            host="127.0.0.1", database ='mydb')
        cursor = cnx.cursor()
        #query = ("INSERT INTO host (hostID, playlistID, spotifyToken, spotifyUsername) VALUES (2, bcc, abc, abb);")
        query = ("INSERT INTO host (hostID, playlistID, spotifyToken, spotifyUsername) "
           "VALUES(%s, %s, %s, %s)")
        data = ("2", "bcc", "abc", "abb")
        cursor.execute(query, data)
        for (hostID, playlistID, spotifyToken, spotifyUsername) in cursor:
            print("{}, {}, {}, {}".format(
            hostID, playlistID, spotifyToken, spotifyUsername))
        cursor.close()
        cnx.commit()
        cnx.close()
    

    def printing(self):
        cnx = mysql.connector.connect(user='root', password ="mynewpassword", 
            host="127.0.0.1", database ='mydb')
        cursor = cnx.cursor()
        for (hostID, playlistID, spotifyToken, spotifyUsername) in cursor:
            print("{}, {}, {}, {}".format(
            hostID, playlistID, spotifyToken, spotifyUsername))
        cursor.close()
        cnx.close()
    #for (eventID, eventStatus, hostID, explicit) in self.cursor:
    #   print("{}, {}, {}, {}".format(
    #  eventID, eventStatus, hostID, explicit))

#define API endpoints
api.add_resource(CreateUser, '/CreateUser')
api.add_resource(SendVote, '/SendVote')

if __name__ == '__main__':
    
    db = Database()
    db.insertNewHost("2", "11", "22", "dummy")
    #db.printing()
    #db.insertNewEvent("3", "on", "2", "0", "my")

    

app.run(debug=True)