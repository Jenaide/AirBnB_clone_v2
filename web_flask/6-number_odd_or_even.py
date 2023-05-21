#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from flask import Flask, render_template
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

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """A dynamic route that displays n as an integer only if its a number"""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def integer_n(n):
    """ROute that display n is an integer on an html page"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ROute that display n is an even|odd on an html page"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
