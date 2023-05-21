#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """uses storage to fetch data from the storage engine"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_states():
    """"Display a HTML page inside the tag BODY""""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
