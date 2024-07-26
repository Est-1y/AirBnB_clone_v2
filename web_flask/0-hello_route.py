#!/usr/bin/python3
""" Script starting a Flask web application  listening on 0.0.0.0, port 5000"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """through route to print web"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
