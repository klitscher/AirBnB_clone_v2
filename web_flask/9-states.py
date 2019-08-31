#!/usr/pin/python3
"""Module to start a Flask web application"""

from models import storage
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """Closes current SQLAlchemy session after each request"""
    storage.close()


@app.route('/states_list')
def state_list():
    """Injects states and info into html"""
    states = storage.all('State')
    return render_template('7-states_list.html', state=states)


@app.route('/cities_by_states')
def city_list():
    """Injects the cities into html"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', state=states)


@app.route('/states')
def states():
    """Injects states and info into html"""
    states = storage.all('State')
    return render_template('9-states.html', state=states)


@app.route('/states/<id>')
def state_id_list(id):
    """Injects state and cities into html based on state id"""
    states = storage.all('State')
    if ("State.{}".format(id)) in states:
        state = states.get("State." + id)
    else:
        state = "None"
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
