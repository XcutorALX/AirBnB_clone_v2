#!/usr/bin/python3
"""
    This script starts a Flask web application
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Root root for flask app
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        hbnb route for flask app
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
        /c route for flask app
    """
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
        /python route for flask app
    """
    return f"Python {escape(text).replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        number route for flask app
    """

    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
