#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created by Jenaide Sibolie
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """flask route that returns Hello hbnb"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """flask route that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text=None):
    """A dynamic text input and replace _ with a space and show the text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """A dynamic text input and replace _ with space and show text"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
