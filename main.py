import json

from flask import Flask
from flask_restful import Resource, Api
from Cwiczenia7.Import import read_file
from Cwiczenia7.Klasa import Movie
from Cwiczenia7.Linki import Linki
from Cwiczenia7.rating import Rating
from Cwiczenia7.Tagi import Tags
from flask import url_for

app = Flask(__name__)
api = Api(app)

class Movies(Resource):
    def get(self):
        film = read_file('./API/movies.csv')
        Filmy = list()
        for row in film:
            Filmy.append(Movie(row.split(',')[0],row.split(',')[1],row.split(',')[2]).__dict__)
        return Filmy



class Link(Resource):
    def get(self):
        link = read_file('./API/links.csv')
        links = list()
        for row in link:
            links.append(Linki(row.split(',')[0],row.split(',')[1],row.split(',')[2]).__dict__)
        return links


class Ratingi(Resource):
    def get(self):
        rat = read_file('./API/ratings.csv')
        ratings = list()
        for row in rat:
            ratings.append(Rating(row.split(',')[0],row.split(',')[1],row.split(',')[2],row.split(',')[3]).__dict__)
        return ratings


class Tag(Resource):
    def get(self):
        tag = read_file('./API/tags.csv')
        tagi = list()
        for row in tag:
            tagi.append(Tags(row.split(',')[0],row.split(',')[1],row.split(',')[2],row.split(',')[3]).__dict__)
        return tagi


api.add_resource(Tag, '/Tagi')
api.add_resource(Ratingi, '/Oceny')
api.add_resource(Movies, '/Filmy')
api.add_resource(Link, '/Links')
if __name__ == '__main__':
    app.run(debug=True)