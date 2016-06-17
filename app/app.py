'''
Subsidietrekker.nl

app.py

'''

from flask import Flask

app = Flask(__name__)


app.config['SECRET_KEY'] = 'iUH@#$OIHF(qa8f3oihjq32r'


ES_SETTINGS = {
    'ES_CLUSTER': 'http://localhost:9200',
    'ES_INDEX': 'sub',
    'ES_TYPE': 'item',
}
