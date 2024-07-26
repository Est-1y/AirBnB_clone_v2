#!/usr/bin/python3
""" Script starting a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """through route Printing Web """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """through route Print Web """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Printing char C"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ through route printing python"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
