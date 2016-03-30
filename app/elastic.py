'''
Subsidietrekker.nl

Elastic.py

'''
from elasticsearch import Elasticsearch

ES_CLUSTER = 'http://localhost:9200'
ES_INDEX = 'sub'
ES_TYPE = 'item'
es = Elasticsearch(ES_CLUSTER)


def receiver(form_data):
    '''receive input from form '''
    pass


def query_builder(cleaned_data):
    ''' build ES query using cleaned data from receiver '''
    pass



def query_es(query_data):
    ''' query ES '''
    pass


def pass_to_table(query_results):
    ''' pass query results to datatables '''
    pass


def pass_to_viz(query_results):
    ''' pass query results to d3 '''
    pass