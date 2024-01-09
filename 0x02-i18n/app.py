#!/usr/bin/env python3
"""This is a simple Flask app"""
import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Union, Dict
import pytz


class Config:
    """Configuration for application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """Uses reques to find the best locale match"""
    options = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """Mock user authentication"""
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """Sets the global user"""
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))
    setattr(g, 'time', format_datetime(datetime.datetime.now()))


@babel.timezoneselector
def get_timezone() -> str:
    """Sets the appropriate timezone"""
    tz = request.args.get('timezone', None)
	if tz:
		try:
			return timezone(tz).zone
		except pytz.exceptions.UnknownTimeZoneError:
			pass
	if g.user:
		try:
			tz = g.user.get('timezone')
			return timezone(tz).zone
		except pytz.exceptions.UnknownTimeZoneError:
			pass

	default_tz = app.config['BABEL_DEFAULT_TIMEZONE']
	return default_tz
    

@app.route('/')
def home() -> str:
    """Returns a render of the specified html template"""
    return render_template('index.html')
