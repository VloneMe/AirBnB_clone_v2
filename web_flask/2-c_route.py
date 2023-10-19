#!/usr/bin/python3
"""
A script that starts a Flask web application.
"""

from flask import Flask

"""
# Create a Flask web application"""
app = Flask(__name__)

""""
A route for the root URL ('/') with strict_slashes=False.
"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# A route for '/hbnb' with strict_slashes=False
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

"""
A route that takes a text parameter and displays it
"""
@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """
    This replaces underscores with spaces in the text parameter
    """
    text = text.replace('_', ' ')
    return "C " + text

if __name__ == '__main__':
    """ This runs the Flask app on 0.0.0.0 and port 5000 """
    app.run(host='0.0.0.0', port=5000)
