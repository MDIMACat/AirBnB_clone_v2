#!/usr/bin/python3
"""Generates a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """Greeting method"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB METHOD"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
