#!/usr/bin/env python3
"""Flask app Babel Extension"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """babel config class for flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine best match for a web page"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def welcome_page() -> str:
    """renders a welcome page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
