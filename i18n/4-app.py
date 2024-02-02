#!/usr/bin/env python3
"""Babel locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """Class to configure language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def my_home():
    """Method template that simply outputs a message"""
    return render_template('./4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
