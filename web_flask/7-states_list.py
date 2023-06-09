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
    """uses Storage to fetch data from the storage engine"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """Display a HTML page inside the tag BODY"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
