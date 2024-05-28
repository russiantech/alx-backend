#!/usr/bin/env python3
"""
Flask app with Babel setup for internationalization
and template parametrization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages or\
            use the locale provided in the URL.

    Returns:
        str: The best match locale.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Route handler for the root URL. Renders the index.html template.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
