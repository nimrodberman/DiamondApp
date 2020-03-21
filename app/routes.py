from app import app
from app.SearchForm import SearchForm
from app.PhotoForm import UploadForm
from flask import render_template, flash, redirect,request
from flask import g
import sqlite3


# Website Homepage
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


# Manual Search
@app.route('/')
@app.route('/Search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        cur = get_db().cursor()
        sr = cur.execute("""SELECT * FROM diamonds WHERE shape=? AND size=? 
         AND color=? AND clarity=? AND cut=? AND florecent=?""", (form.shape.data, form.size.data, form.color.data,
                                                                  form.clarity.data, form.cut.data
                                                                  , form.florecent.data)).fetchone()
        # convert sql text to diamond class
        diamond = Diamond(form.shape.data, form.size.data,  form.color.data,  form.clarity.data, form.cut.data,
                          form.florecent.data, "Diamond type do not exist in the database")
        if sr is not None:
            diamond.price = sr[6]

        return search_result(diamond)
    return render_template('Search.html', form=form)


# Picture Search
@app.route('/')
@app.route('/Search_by_image', methods=['GET', 'POST'])
def search_by_image():
    form = UploadForm()
    if form.validate_on_submit():
        # read the certificate text
        text = ""

        # create an diamond instance
        diamond = Diamond(text[0], text[1],  text[2],  text[3],
                          text[4], text[5], "Diamond type do not exist in the database")

        # extract diamond price
        cur = get_db().cursor()
        sr = cur.execute("""SELECT * FROM diamonds WHERE shape=? AND size=? 
         AND color=? AND clarity=? AND cut=? AND florecent=?""", (diamond.shape, diamond.size,
                                                                  diamond.color, diamond.clarity, diamond.cut
                                                                  , diamond.florecent)).fetchone()
        if sr is not None:
            diamond.price = sr[6]

        # return the result
        return search_result(diamond)

    return render_template('Search_by_image.html', form=form)


# The search result
@app.route('/')
@app.route('/Search_result')
def search_result(diamond):
    return render_template('Search_result.html', diamond=diamond)


# Database getter
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('diamond.db')
    return db


# Database closer
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# diamond object
class Diamond:
    def __init__(self, shape , size, color, clarity, cut, florecent,price):
        self.shape = shape
        self.size = size
        self.color = color
        self.clarity = clarity
        self.cut = cut
        self.florecent = florecent
        self.price = price
