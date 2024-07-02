#!/usr/bin/env python3
"""_summary_
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """_summary_
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """_summary_

    Returns:
        Any: _description_
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
