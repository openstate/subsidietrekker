'''

Subsidietrekker.nl

streamer.py

'''

import json
from flask import request
from flask_cors import cross_origin
from elasticsearch import Elasticsearch
from app import app, ES_SETTINGS


es = Elasticsearch(ES_SETTINGS['ES_CLUSTER'])


# @app.route('/_form_streamer', methods=['GET', 'POST'])
# def form_streamer():
#     simple_search_dump = request.args.get('overheid')

#     # print simple_search_dump
#     return(simple_search_dump)


@app.route('/_streamer', methods=['GET'])
@cross_origin()
def streamer():
    '''
    Streamer function.
    Offers ElasticSearch index data to DataTables asynchronously.
    '''
    result = {}

    # Get current values from datatables
    search = request.args.get('search[value]', u'')
    draw = request.args.get('draw')
    columns = ['overheid', 'ontvanger', 'realisatie', 'jaar', 'beleid', 'regeling']
    order_column_index = request.args.get('order[0][column]', '0')
    try:
        order_column = columns[int(order_column_index)]
    except (IndexError, ValueError) as e:
        order_column = 0
    direction = request.args.get('order[0][dir]', 'asc')

    # Check for active search fields
    fields = []
    available_fields = ['overheid', 'ontvanger', 'beleid', 'regeling']
    for field in available_fields:
        if request.args.get('buttons[%s]' % (field,)) == u'true':
            fields.append(field)

    # Create the ElasticSearch simple_query_string

    if unicode(search).strip() != u'':
        query_part = {"query": {
            "multi_match": {
                "type": 'phrase_prefix',
                "query": search,
                "slop": 10,
                "analyzer": "snowball",
                "fields": fields,
            }
        }}
    else:
        query_part = {}

    es_query = {
        "sort": {order_column: {"order": direction}} # FIX
    }
    es_query.update(query_part)
    print "stream:", es_query
    # Query the ES index using the elasticsearch module
    query = es.search(index=ES_SETTINGS['ES_INDEX'], size=request.args.get('length'), from_=request.args.get('start'), body=es_query)

    # Collect total records in ES index
    total_set = es.search(index=ES_SETTINGS['ES_INDEX'])
    total_records = total_set['hits']['total']

    # Collect found results
    found_set = query
    found_total_records = found_set['hits']['total']
    found_results = [result['_source'] for result in found_set['hits']['hits']]

    # Create dict of results
    result['draw'] = draw
    result['recordsTotal'] = total_records
    result['recordsFiltered'] = found_total_records
    result['data'] = found_results

    # Jsonify and return the results
    return json.dumps(result)



@app.route('/_viz_streamer')
@cross_origin()
def viz_streamer():

    search = request.args.get('query', u'')
    fields = []
    available_fields = ['overheid', 'ontvanger', 'beleid', 'regeling']
    for field in available_fields:
        if request.args.get('buttons[%s]' % (field,)) == u'true':
            fields.append(field)

    if unicode(search).strip() != u'':
        query_part = {"query": {
            "multi_match": {
                "type": 'phrase_prefix',
                "query": search,
                "slop": 10,
                "analyzer": "snowball",
                "fields": fields
            }
        }}
    else:
        query_part = {}

    es_query = {
        "size": 0,
        "aggs": {
            "ontvangers": {
                "terms": {
                    "field": "ontvanger.raw",
                    "order" : { "realisatie.sum" : "desc" }
                },
                "aggs": { "realisatie": { "stats" : { "field" : "realisatie" } } }
            }
        }
    }
    es_query.update(query_part)

    query = es.search(index=ES_SETTINGS['ES_INDEX'], body=es_query)



    hits = query['aggregations']['ontvangers']['buckets']
    data = [hit for hit in hits]

    print 'viz: ', es_query
    return json.dumps(data)
