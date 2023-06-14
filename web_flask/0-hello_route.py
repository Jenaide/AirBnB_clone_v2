#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Starts a flask app and returns Hello HBNB!"""
    return render_template("10-hbnb_filters.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
