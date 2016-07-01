'''
Subsidietrekker.nl

views.py

'''

from flask import render_template, request
from app import app

# index view
@app.route('/')
def home():
    return render_template('index.html')

# data view
@app.route('/data')
def over_data():
    return render_template('over_data.html')

# contact view
@app.route('/contact')
def contact():
    return render_template('contact.html')
