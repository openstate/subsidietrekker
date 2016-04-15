'''
Subsidietrekker.nl

views.py

'''

from flask import render_template, request
from app import app
from forms import SimpleSearch

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    form = SimpleSearch()
    if request.method == 'POST':
        print form.data
        return json.dumps(receiver(**form.data))
    elif request.method == 'GET':
        return render_template('demo.html', form=form)

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
