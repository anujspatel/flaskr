# all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from contextlib import closing
from sqlalchemy import *
from database import db_session, init_db
from models import Post
from sqlalchemy.ext.declarative import declarative_base

# configuration
DATABASE = 'postgres://jyyhdwzznpxdui:J95RiTuce6sLygy1LHff5nsKrc@ec2-54-83-29-133.compute-1.amazonaws.com:5432/dbi5flsrif9i9v'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
initdb_command()

def print_All_Entries():
    for post in db_session.query(Post).order_by(Post.id):
        print(post.title, post.text)

@app.route('/')
def show_entries():
    entries = Post.query.all()
    entries = entries[::-1]
    entries_dict = {}
    for i in entries:
        entries_dict[i.title] = i.text
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    entry_Title = request.form['title']
    entry_Text = request.form['text']
    p = Post(entry_Title, entry_Text)
    db_session.add(p)
    db_session.commit()
    flash('New entry was successfully posted!')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username, fucker.'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password, fucker.'
        else:
            session['logged_in'] = True
            flash('You are now logged in, fucker.')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You are now logged out, fucker.')
    return redirect(url_for('show_entries'))