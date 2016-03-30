'''
Subsidietrekker.nl

Elastic.py

'''
from elasticsearch import Elasticsearch


# connect to ES and create ElasticSearch instance
ES_CLUSTER = 'http://localhost:9200'
ES_INDEX = 'sub'
ES_TYPE = 'item'
es = Elasticsearch(ES_CLUSTER)

#receive input from form
def receiver(form_data):
    pass


# build ES query using cleaned data from receiver
def query_builder(cleaned_data):
    pass


#query ES
def query_es(query_data):
    pass


# pass query results to front
def pass_to_table(query_results):
    pass


def pass_to_viz(query_results):
    pass