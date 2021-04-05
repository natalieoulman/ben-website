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


@app.route('/benviews')
def ben_reviews():
    """Returns a review page of Ben's work"""

    return render_template('benviews.html')


@app.route('/bens-contact')
def ben_contact():
    """Returns a contact page for Ben"""

    return render_template('bens_contact.html')


@app.route('/bens-fees')
def ben_fee():
    """Returns a list of fees for Ben's services"""

    return render_template('bens_fees.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
