#!/usr/bin/python3
"""
Define a module to serve requests for
states.
"""
from models.state import State
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Shows list of all states"""
    states = storage.all(State)
    return render_template("7-states_list.py", states=states)


@app.teardown_appcontext
def end_session():
    """Removes SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
