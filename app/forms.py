'''
Subsidietrekker.nl

forms.py


Holds the different form classes. Uses wtforms and the flask_wtf wrapper
'''

from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField

class SimpleSearch(Form):
    zoekterm = StringField('Zoeken..')
    overheid = BooleanField('Overheid')
    ontvanger = BooleanField('Ontvanger')
    regeling = BooleanField('Regeling')
    beleidsartikel = BooleanField('Beleidsartikel')

class VizOptions(Form):
    stats = SelectField(label='Stats', choices=[('count', 'aantal'), ('min', 'minimum'), ('max', 'maximum'), ('avg', 'gemiddelde'), ('sum', 'som')])

# class CompareSearch(Form):
#     zoekterm = StringField('Zoekterm..')


# class VizOptions(Form):
#     pass
