#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    return '<ul>' + \
    '<li>ID: {}</li>'.format(id) + \
    '<li>Name: {}</li>'.format(id) + \
    '<li>Species: {}</li>'.format(id) + \
    '<li>Zookeeper: {}</li>'.format(id) + \
    '<li>Enclosure: {}</li>'.format(id) + \
    '</ul>'



@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    return ''

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    return ''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
