#!/usr/bin/env python3

"""
A basic flask app
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """_summary_

    Returns:
        Any: _description_
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
