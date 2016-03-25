# '''
# Subsidietrekker.nl

# models.py

# '''

# from flask_wtf import Form
# from wtforms import StringField, IntegerField, DateTimeField, SubmitField
# from wtforms.validators import InputRequired

# from elasticsearch import Elasticsearch


# '''Forms'''
# class SubmitSubsidieForm(Form):
#     overheid = StringField('Overheid', validators=[InputRequired()])
#     regeling = StringField('Regeling', validators=[InputRequired()])
#     ontvanger = StringField('Ontvanger', validators=[InputRequired()])
#     beleidsartikel = StringField('Beleidsartikel', validators=[InputRequired()])
#     realisatie = IntegerField('Realisatie', validators=[InputRequired()])
#     jaar = DateTimeField('Jaar', validators=[InputRequired()])
#     submit = SubmitField('Submit')


# '''Elastic Search'''
# es_config = {
#     'ES_CLUSTER': 'http://localhost:9200',
#     'ES_INDEX': 'sub',
#     'ES_TYPE': 'item'
# }

# es = Elasticsearch(es_config['ES_CLUSTER'])

