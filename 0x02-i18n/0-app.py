#!/usr/bin/env python3

"""
A basic flask app
"""

from flask import Flask, render_template
from typing import Any


app = Flask(__name__)


@app.route('/')
def index() -> Any:
    """_summary_

    Returns:
        Any: _description_
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
