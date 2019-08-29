#!/usr/pin/python3
"""Module to start a Flask web application"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False
app.run(host='0.0.0.0')


@app.route('/')
def hello_world():
    """Function to print something"""
    return "Hello HBNB!"
