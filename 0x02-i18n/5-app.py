#!/usr/bin/env python3
"""
This script initializes a Flask application
with internationalization support using Flask-Babel.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
from typing import Any, Dict

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
    request_locale = request.args.get('locale')
    if request_locale and request_locale in app.config['LANGUAGES']:
        return request_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> Any:
    """
    Render the index page template.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
