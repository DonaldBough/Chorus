from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class CreateEvent(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, help='Name of the Event')
            parser.add_argument('password', type=str, help='Password for the Event')
            args = parser.parse_args()

            #_eventName     = args['name']
            #_eventPassword = args['password']

            return {'Name': args['name'], 'Password': args['password']}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(CreateEvent, '/CreateEvent')

if __name__ == '__main__':
    app.run(debug=True)
