"""Server for ben's website."""

from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
import requests
import json

app = Flask(__name__)
app.secret_key = "ranchdressing"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Returns landing page of ben's site"""

    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
