#!/usr/bin/env python3
"""
This script initializes a Flask application
with internationalization support using Flask-Babel.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match language based on Accept-Language header.
    """
    request_options = [
        request.args.get('locale'),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
        ]
    for locale in request_options:
        if locale and locale in Config.LANGUAGES:
            return locale


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page template.
    """
    return render_template('6-index.html')


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """_summary_

    Returns:
        Dict | None: _description_
    """
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """_summary_
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
