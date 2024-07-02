#!/usr/bin/env python3
"""Basic Flask app to render a welcome page"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome_page() -> str:
    """Renders a welcome page from template

    Returns:
        the html welcome page
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
