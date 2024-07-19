#!/usr/bin/env python3

"""
A basic Flask app with a single route
that renders a template.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    The index route that renders the
    0-index.html template.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
