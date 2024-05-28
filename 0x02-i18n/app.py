#!/usr/bin/env python3
"""
Flask app with Babel setup for internationalization,
template parametrization,
mock login, timezone selection, and current time display.
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime
import sys


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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """
    Return a user dictionary if the user ID is found, otherwise None.

    Returns:
        dict: User dictionary or None.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """
    Before request function to set the user globally.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages or\
            use the locale provided in the URL.

    Returns:
        str: The best match locale.
    """
    # Priority 1: Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Priority 2: Locale from user settings
    user = g.get('user')
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']

    # Priority 3: Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the appropriate time zone.

    Returns:
        str: The appropriate time zone.
    """
    # Priority 1: Timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    # Priority 2: Timezone from user settings
    user = g.get('user')
    if user:
        try:
            pytz.timezone(user['timezone'])
            return user['timezone']
        except UnknownTimeZoneError:
            pass

    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """
    Route handler for the root URL. Renders the index.html template.

    Returns:
        str: Rendered HTML content for the index page.
    """
    # Get the current time in the appropriate time zone
    current_time = datetime.now(pytz.timezone(get_timezone()))
    formatted_time = current_time.strftime('%b %d, %Y, %I:%M:%S %p')

    return render_template('8-index.html', current_time=formatted_time)


if __name__ == '__main__':
    port = 5000  # default port
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(debug=True, port=port)
