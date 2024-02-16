#!/usr/bin/python3
"""
Generates a Flask web application
"""

from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes = False)
def greeting():
    """Greeting method"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes = False)
def hbnb():
    """HBNB METHOD"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes = False)
def c_text(text):
    """C text method"""
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes = False)
@app.route('/python/<text>', strict_slashes = False)
def python_text(text="is cool"):
    """Python text method"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes = False)
def number(n):
    """Route to a whole number
    Args: n (Integer): a whole number
    """
    if n.isdigit() == True:
        return f"{n} is a number" 
    else:
        abort(404)

     
@app.route('/number_template/<n>')
def numTemp(n):
    """ Renders a template if its a whole number
    Args:
        n (Int): a whole number
    """
    if n.isdigit() == True:
        return render_template('5-number.html', number=n)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
