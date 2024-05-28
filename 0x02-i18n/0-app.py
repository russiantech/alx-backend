#!/usr/bin/env python3
"""
Basic Flask app module.
"""

from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Route handler for the root URL. Renders the index.html template.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
