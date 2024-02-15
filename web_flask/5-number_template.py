#!/usr/bin/python3
"""Generates a Flask web application
"""

from flask import Flask, abort, render_template
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def greeting():
    """Greeting method
    """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """HBNB METHOD
    """
    return "HBNB"

@app.route('/c/<text>')
def c_text(text):
    """
    C text method
    """
    text = text.replace('_', ' ')
    return f"C {escape(text)}"

@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """
    Python text method
    """
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"

@app.route('/number/<n>')
def number(n):
    """Check if n is a digit and the displays it

    Args:
        n (Integer): a whole number
    """
    if n.isdigit() == True:
        return f" {n} is a number" 
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
