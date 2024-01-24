#!/usr/bin/env python3
"""Babel locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """Class to configure language"""
    LANGUAGES = ["en", "fr"]


app.config.from_object('2-app.Config')
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@app.route('/')
def my_home():
    """Method template that simply outputs a message"""
    return render_template('./2-index.html')


def get_locale():
    """get_locale Determine the best match with
    our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
