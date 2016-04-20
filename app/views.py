'''
Subsidietrekker.nl

views.py

'''

from flask import render_template, request
from app import app
from forms import SimpleSearch, VizOptions

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    searchform = SimpleSearch()
    vizform = VizOptions()
    return render_template('demo.html', form=searchform, vizform=vizform)

@app.route('/data')
def over_data():
    return render_template('over_data.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/viz')
def viz():
    return render_template('viz.html')
