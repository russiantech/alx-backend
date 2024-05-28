#!/usr/bin/env python3
"""
Flask app with Babel setup for internationalization.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
babel: Babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Route handler for the root URL. Renders the index.html template.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
