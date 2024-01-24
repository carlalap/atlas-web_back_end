#!/usr/bin/env python3
"""task2. Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel
from babel import get_locale

app = Flask(__name__)
babel = Babel(app)


class Config():
    """Class to configure language"""
    LANGUAGES = ["en", "fr"]


BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_TIMEZONE = "UTC"
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine the best match with
    our supported languages."""
    user_languages = request.accept_languages
    best_match = user_languages.best_match(app.config['LANGUAGES'])

    return best_match


@app.route('/')
def my_home():
    """Method template that simply outputs a message"""
    return render_template('./0-index.html')


if __name__ == '__main__':
    app.run()
