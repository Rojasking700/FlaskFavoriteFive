from app import app
from flask import render_template

class Artist():

    def __init__(self, genre ,artist, s1, s2, s3, s4, s5): #this intializes all of the data
        self.genre = genre
        self.artist = artist
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5

    def dict(self): # this creates a dictionary that can be used in the html to refernce all the data
        
        dic = {
            'title': self.genre,
            'artist': self.artist,
            'songs': [ self.s1,self.s2,self.s3,self.s4,self.s5]
            # 's2': 
            # 's3': 
            # 's4': 
            # 's5': 
        }
        if self.genre == 'rock': # if genre  = rock then it will add it to the rock genre
            rocks[self.artist]= dic
        elif self.genre == 'rap':
            raps[self.artist]= dic
        elif self.genre == 'country':
            countrys[self.artist]= dic
        elif self.genre == 'mexican':
            mexicans[self.artist]= dic
        # print(rock)
        return dic



@app.route('/')
@app.route('/index')
def hello_world():

    title = "Hello World"
    return render_template('index.html', title=title)
#************************************************************
raps = {
    'title': 'rap' #this diction is for all of the artist of the rap genre
}
@app.route('/rap')
def rap():
    trippie = Artist('rap','trippie_redd','Bang','Taking a Walk','Weee','Dark Knight','Shake it Up')
    trippie.dict()
    title = 'Rap'
    return render_template('rap.html', **raps)
#************************************************************
rocks = {
    'title': 'rock' #this diction is for all of the artist of the rock genre
}
@app.route('/rock')
def rock():
    motionless = Artist('rock','Motionless_in_White','Another Life','Somebody Told Me','Eternally Yours','Disguise','Voices') #this intializes the band motionless in white
    motionless.dict() #this runs the dict function
    title = 'Rock'
    return render_template('rock.html', **rocks)
#************************************************************
countrys = {
    'title': 'country' #this diction is for all of the artist of the rock genre
}
@app.route('/country')
def country():
    Morgan = Artist('country','Morgan_Wallen','7 summers','whiskey glasses','Chasin you','Wasted on You','865')
    Morgan.dict()
    title = 'Country'
    return render_template('country.html', **countrys)
#************************************************************
mexicans = {
    'title': 'mexican' #this diction is for all of the artist of the rock genre
}
@app.route('/mexican')
def mexican():
    t3r = Artist('mexican','T3R_Elemento','Ojitos de conejo','Garantia de Calidad','El Oso', 'Amigo de la Muerte', 'Jalo y exajalo')
    t3r.dict()
    title = 'Mexican'
    return render_template('mexican.html', **mexicans)