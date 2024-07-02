#!/usr/bin/env python3
"""Flask app Babel Extension"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """babel config class for flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def welcome_page() -> str:
    """renders a welcome page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
