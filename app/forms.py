'''
Subsidietrekker.nl

forms.py


Holds the different form classes. Uses wtforms and the flask_wtf wrapper
'''

from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, SubmitField, BooleanField #, SelectField
from wtforms.validators import InputRequired

# class SubmitSubsidieForm(Form):
#     overheid = StringField('Overheid', validators=[InputRequired()])
#     regeling = StringField('Regeling', validators=[InputRequired()])
#     ontvanger = StringField('Ontvanger', validators=[InputRequired()])
#     beleidsartikel = StringField('Beleidsartikel', validators=[InputRequired()])
#     realisatie = IntegerField('Realisatie', validators=[InputRequired()])
#     jaar = DateTimeField('Jaar', validators=[InputRequired()])
#     submit = SubmitField('Submit')

class SimpleSearch(Form):
    zoekterm = StringField('Zoeken..')
    overheid = BooleanField('Overheid')
    ontvanger = BooleanField('Ontvanger')
    regeling = BooleanField('Regeling')
    beleidsartikel = BooleanField('Beleidsartikel')
    submit = SubmitField('Submit')

class CompareSearch(Form):
    zoekterm = StringField('Zoekterm..')


class VizOptions(Form):
    pass

'''

compare search:
stats

jaartal.

Other options:
Scale (internat ,.., gemeente)
Realisatie (min, max, avg, etc.)


'''
