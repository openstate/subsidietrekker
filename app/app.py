'''
Subsidietrekker.nl

app.py

'''

from flask import Flask

app = Flask(__name__)

def add_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, PATCH, DELETE, OPTIONS'
    return response

app.after_request(add_cors_header)

# flask Secret Key
app.config['SECRET_KEY'] = 'iUH@#$OIHF(qa8f3oihjq32r'

# Elastic Search settings
ES_SETTINGS = {
    'ES_CLUSTER': 'http://c-subsidietrekker-elasticsearch:9200',
    'ES_INDEX': 'sub',
    'ES_TYPE': 'item',
}
