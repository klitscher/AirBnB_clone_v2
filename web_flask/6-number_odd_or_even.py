#!/usr/pin/python3
"""Module to start a Flask web application"""

from flask import Flask
from flask import render_template

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


@app.route('/python/')
@app.route('/python/<text>')
def python_variable(text='is cool'):
    """Function to display more variable text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def number_variable(n):
    """Returns number if it is an int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def html_variable(n):
    """Injects a variable into html page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    """Injects odd or even into an html page"""
    if n % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    return render_template(
        '6-number_odd_or_even.html', n=n, even_or_odd=odd_even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
