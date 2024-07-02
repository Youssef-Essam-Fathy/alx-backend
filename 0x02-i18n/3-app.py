#!/usr/bin/env python3
"""_summary_
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
from typing import Any


class Config:
    """_summary_
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
    Determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> Any:
    """_summary_

    Returns:
        Any: _description_
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
