#!/usr/bin/python3
"""Generates a Flask web application
"""

from flask import Flask, abort, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """Greeting method
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB METHOD
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    C text method
    """
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def python_text(text="is cool", strict_slashes=False):
    """
    Python text method
    """
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Check if n is a digit and the displays it

    Args:
        n (Integer): a whole number
    """
    if n.isdigit() is True:
        return f" {int(n)} is a number"
    else:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def numTemp(n):
    """ Renders a template if its a whole number
    Args:
        n (Int): a whole number
    """
    if n.isdigit() is True:
        return render_template('5-number.html', number=int(n))
    else:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def evenOdd(n):
    """ Renders a template if its an even and odd number
    Args:
        n (Int): a whole number
    """
    if n.isdigit() is True:
        if (int(n) % 2 == 0):
            return render_template('6-number_odd_or_even.html', enum=int(n))
        else:
            return render_template('6-number_odd_or_even.html', onum=int(n))
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
