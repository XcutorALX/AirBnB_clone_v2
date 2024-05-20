#!/usr/bin/python3
"""
    This script starts a Flask web application
"""
from flask import Flask


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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
