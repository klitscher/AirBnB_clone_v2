#!/usr/pin/python3
"""Module to start a Flask web application"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    """Function to print something"""
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    """Function to print something"""
    return "HBNB!"


@app.route('/c/<text>')
def variables(text):
    """Function to display variable text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
