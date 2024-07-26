#!/usr/bin/python3
"""
Starts a Flask web application
listens on 0.0.0.0, port 5000.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """eliminate current session of sqlalchemist"""
    storage.close()


@app.route('/states_list')
def states_list():
    """
    Printing an HTML page with a list of all State objects in DBStorage
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
