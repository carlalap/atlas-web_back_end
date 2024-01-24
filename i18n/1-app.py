#!/usr/bin/env python3
"""task1. Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)



class Config():
    """Class to configure language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)


@app.route('/')
def my_home():
    """Method template that simply outputs a message"""
    return render_template('./0-index.html')


if __name__ == '__main__':
    app.run()
