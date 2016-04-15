'''
Subsidietrekker.nl

forms.py


Holds the different form classes. Uses wtforms and the flask_wtf wrapper
'''

from flask_wtf import Form
from wtforms import StringField, BooleanField

class SimpleSearch(Form):
    zoekterm = StringField('Zoeken..')
    overheid = BooleanField('Overheid')
    ontvanger = BooleanField('Ontvanger')
    regeling = BooleanField('Regeling')
    beleidsartikel = BooleanField('Beleidsartikel')

# class CompareSearch(Form):
#     zoekterm = StringField('Zoekterm..')


# class VizOptions(Form):
#     pass
