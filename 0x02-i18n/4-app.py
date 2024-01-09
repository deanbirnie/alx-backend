#!/usr/bin/env python3
"""This is a simple Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
config = app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Uses reques to find the best locale match"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """Returns a render of the specified html template"""
    return render_template('4-index.html')
