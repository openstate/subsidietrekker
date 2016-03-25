'''
Subsidietrekker.nl

Elastic.py

'''
from elasticsearch import Elasticsearch

ES_CLUSTER = 'http://localhost:9200'
ES_INDEX = 'sub'
ES_TYPE = 'item'
es = Elasticsearch(ES_CLUSTER)
