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

#db stuff
cnx = mysql.connector.connect(user='root', passswd="ChorusIsNumber1", host="174.138.64.25", database='mydb')
cursor = cnx.cursor()

cursor.execute("SELECT * FROM event")

for (eventID, eventStatus, hostID, explicit) in cursor:
  print("{}, {}, {}, {}".format(
    eventID, eventStatus, hostID, explicit))

cursor.close()
cnx.close()

#define API endpoints
api.add_resource(CreateUser, '/CreateUser')
api.add_resource(SendVote, '/SendVote')

if __name__ == '__main__':
    app.run(debug=True)