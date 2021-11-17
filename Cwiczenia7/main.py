import json

from flask import Flask
from flask_restful import Resource, Api
from Import import read_file
from Klasa import Movie

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        dane = read_file('./API/movies.csv')
        Filmy = list()
        for row in dane:
            Filmy.append(Movie(row.split(',')[0],row.split(',')[1],row.split(',')[2]).__dict__)
        return Filmy

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)