#!/usr/bin/python3
"""
    This script starts a Flask web application
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
        states_list route for flask app
    """

    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


@app.route('/states/<id>', strict_slashes=False)
def states_list():
    """
        states_list route for flask app
    """

    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    """
        Teardown function
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
