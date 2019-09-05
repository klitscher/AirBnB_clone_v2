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


@app.route('/hbnb')
def display_HBNB():
    """Code to display our HBNB landing page"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
