'''
Subsidietrekker.nl

Elastic.py

'''
import json
from flask import request
from elasticsearch import Elasticsearch
from app import app

ES_CLUSTER = 'http://localhost:9200'
ES_INDEX = 'sub'
ES_TYPE = 'item'
es = Elasticsearch(ES_CLUSTER)


def receiver(**form_data):
    '''receive input from form_data and write it to data_dict'''
    data_dict = dict()
    settings_dict = dict()
    form_dict = dict()

    settings_dict['query_type'] = form_data['query_type']
    settings_dict['table'] = form_data['table']
    settings_dict['viz'] = form_data['viz']
    settings_dict['raw'] = form_data['raw']
    data_dict['settings'] = settings_dict

    form_dict['query'] = form_data['zoekterm']
    fields = [f for f in ['overheid', 'ontvanger', 'regeling', 'beleidsartikel'] if form_data[f]]
    form_dict['fields'] = fields
    data_dict['form'] = form_dict

    print data_dict
    return query_builder(**data_dict)



def query_builder(**cleaned_data):
    ''' build ES query using cleaned data from receiver '''
    query_string =  {
                        "query": {
                            "simple_query_string": {
                                "query": cleaned_data['form']['query'],
                                "analyzer": "snowball",
                                "fields": cleaned_data['form']['fields'],
                                "default_operator": "and"
                            }
                        }
                    }

    return query_es(query_string)





def query_es(query_string):
    ''' query ES '''
    query = es.search(
        index=ES_INDEX, 
        #size=request.args.get('length'), 
        #from_=request.args.get('start'), 
        body=query_string
    )
    pass_to_table(query)
    pass_to_viz(query)

@app.route('/_table_stream')
def pass_to_table(query_results):
    ''' pass query results to datatables '''
    total_docs = es.search(index=ES_INDEX)
    total_records = total_docs['hits']['total']
    records_filtered = query_results['hits']['total']
    draw = request.args.get('draw')

    hits = query_results['hits']['hits']
    data = [hit['_source'] for hit in hits]

    result = {}
    result['draw'] = draw
    result['recordsTotal'] = total_records
    result['recordsFiltered'] = records_filtered
    result['data'] = data

    print data
    return json.dumps(result)


@app.route('/_viz_stream')
def pass_to_viz(query_results):
    ''' pass query results to d3 '''
    pass