from app import app
from flask import render_template

class Artist():

    def __init__(self, genre ,artist, s1, s2, s3, s4, s5):
        self.genre = genre
        self.artist = artist
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5

    def dict(self):
        
        dic = {
            'title': self.genre,
            'artist': self.artist,
            'songs': [ self.s1,self.s2,self.s3,self.s4,self.s5]
            # 's2': 
            # 's3': 
            # 's4': 
            # 's5': 
        }
        if self.genre == 'rock':
            rocks[self.artist]= dic
        # print(rock)
        return dic



@app.route('/')
@app.route('/index')
def hello_world():

    title = "Hello World"
    return render_template('index.html', title=title)

@app.route('/rap')
def rap():
    title = 'Rap'
    return render_template('rap.html', title=title)
rocks = {
    'title': 'rock'
}
@app.route('/rock')
def rock():
    motionless = Artist('rock','Motionless_in_White','Another Life','Somebody Told Me','Eternally Yours','Disguise','Voices') 
    motionless.dict()
    title = 'Rock'
    return render_template('rock.html', **rocks)

@app.route('/country')
def country():
    title = 'Country'
    return render_template('country.html', title=title)

@app.route('/mexican')
def mexican():
    title = 'Mexican'
    return render_template('mexican.html', title=title)