#!/usr/bin/python3
"""Generates a Flask web application
"""

from flask import Flask
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
    return f"C {escape(text)}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
