'''
Subsidietrekker.nl

app.py

'''

from flask import Flask

app = Flask(__name__)

# flask Secret Key
app.config['SECRET_KEY'] = 'iUH@#$OIHF(qa8f3oihjq32r'

# Elastic Search settings
ES_SETTINGS = {
    'ES_CLUSTER': 'http://c-subsidietrekker-elasticsearch:9200',
    'ES_INDEX': 'sub',
    'ES_TYPE': 'item',
}
