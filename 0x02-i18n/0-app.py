#!/usr/bin/env python3
"""This is a simple Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Returns a render of the specified html template"""
    return render_template('0-index.html')
