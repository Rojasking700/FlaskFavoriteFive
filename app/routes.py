from app import app
from flask import render_template


@app.route('/')
@app.route('/')
def hello_world():
    title = "Hello World"
    return render_template('index.html', title=title)

@app.route('/rap')
def rap():
    title = 'Rap'
    return render_template('rap.html', title=title)

@app.route('/rock')
def rock():
    title = 'Rock'
    return render_template('rock.html', title=title)

@app.route('/country')
def country():
    title = 'Country'
    return render_template('country.html', title=title)

@app.route('/mexican')
def mexican():
    title = 'Mexican'
    return render_template('mexican.html', title=title)