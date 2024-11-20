from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate


import requests
import re

# create flask app
app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(message):
    return render_template('error.html', message="Bad Request"), 400


@app.errorhandler(404)
def err_404(message):
    return render_template('error.html', message='404 Page Not Found'), 404


@app.route('/')
def main_page():
    return render_template('index.html', title='Vishnu K V - Homepage')


@app.route('/home')
def home():
    return render_template('base.html', title='Base')

if __name__=='__main__' :
    app.run(debug=True)