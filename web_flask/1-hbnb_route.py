#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """A flask route that return/display hello HBNB"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """A flask route that return/display HBNB"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
