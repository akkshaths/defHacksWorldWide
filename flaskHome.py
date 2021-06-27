from flask import Flask, request, session, g, redirect, \
    url_for, abort, render_template, flash

import datetime
from urllib.request import urlopen as urlopen
import os, sys, json
from clubInterest import Filter
from IPython.display import display


app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('APP_CONFIG_FILE', silent=True)

MAPBOX_ACCESS_KEY = app.config['MAPBOX_ACCESS_KEY']

app.secret_key = 'Bob'


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/afterSignup', methods = ["POST"])
def temp():
    username = request.form.get('email')
    password = request.form.get('pwd')
    age = request.form.get('age')
    name = request.form.get('name')
    email = request.form.get('email')

    #still need to compare with current tings and add to excel file

    return render_template('/interest')

@app.route('/interest')
def interest():
    x = Filter()
    return render_template('interests.html', tableFromTags=x.printting())

@app.route('/inTag', methods = ['POST'])
def tagCalc():
    x = Filter()
    list1 = request.form.getlist()
    y = x.returnClubNames(list1)
    return render_template('interests.html', tableFromTags=y)

@app.route('/scheduler')
def scheduler():
    return render_template('scheduling.html')

@app.route('/map')
def map():
    return render_template('maps.html')



if __name__ == '__main__':
    app.run()