#!/usr/bin/env python3
"""This is a simple Flask app"""
from flask import Flask, render_template
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
def get_locale():
    """Uses reques to find the best locale match"""
    return request.accept_languages.best_match(config)


@app.route('/')
def home():
    """Returns a render of the specified html template"""
    return render_template('3-index.html')
