'''

Subsidietrekker.nl

streamer.py

'''

import json
from flask import request
from elasticsearch import Elasticsearch
from app import app

ES_CLUSTER = 'http://localhost:9200'
ES_INDEX = 'sub'
ES_TYPE = 'item'
es = Elasticsearch(ES_CLUSTER)


@app.route('/_form_streamer', methods=['GET', 'POST'])
def form_streamer():
    simple_search_dump = request.args.get('overheid') 

    # print simple_search_dump
    return(simple_search_dump)


# The new steamer function WIP
@app.route('/_streamer', methods=['GET', 'POST'])
def streamer(simple_search_dump={}):



    da_dump = {}

    # simple_search_dump = request.args.get('overheid') 
    viz_options_dump = {}

    def datatables_streamer():

        result = {}


        search = request.args.get('search[value]')
        draw = request.args.get('draw')
        sort = request.args.get('order[0][dir]')

        fields = []
        available_fields = ['overheid', 'ontvanger', 'beleidsartikel', 'regeling']
        for field in available_fields:
            if request.args.get('buttons[%s]' % (field,)) == u'true':
                fields.append(field)

        es_query = {
                        "query": {
                            "simple_query_string": {
                                "query": search,
                                "analyzer": "snowball",
                                "fields": fields,
                                "default_operator": "and"
                            }
                        },
                        "sort": {"overheid": {"order": sort}}
                    }



        query = es.search(index=ES_INDEX, size=request.args.get('length'), from_=request.args.get('start'), body=es_query)

        total_set = es.search(index=ES_INDEX)
        total_records = total_set['hits']['total']
        
        found_set = query
        found_total_records = found_set['hits']['total']
        found_results = [result['_source'] for result in found_set['hits']['hits']]

        result['draw'] = draw
        result['recordsTotal'] = total_records
        result['recordsFiltered'] = found_total_records
        result['data'] = found_results

        print 'Current searched fields: %s' % fields
        return result


    def d3_streamer():
        
        return {}


    
    datatables_dict = datatables_streamer()
    d3_dict = d3_streamer()

    for d in [datatables_dict, d3_dict]:
        da_dump.update(d)

    # print da_dump
    
    print ('passed dump: %s' % simple_search_dump)
    return json.dumps(da_dump)



@app.route('/_viz_streamer')
def viz_streamer():

    search = request.args.get('query') or 'test'
    fields = []
    available_fields = ['overheid', 'ontvanger', 'beleidsartikel', 'regeling']
    for field in available_fields:
        if request.args.get('buttons[%s]' % (field,)) == u'true':
            fields.append(field)

    es_query = {
                    "query": {
                        "simple_query_string": {
                            "query": search,
                            "analyzer": "snowball",
                            "fields": fields,
                            "default_operator": "and"
                        }
                    },
                    "size": 0,
                    "aggs": {
                        "ontvangers": {
                            "terms": {
                                "field": "ontvanger.raw"
                            }
                        }
                    }
                }


    query = es.search(index=ES_INDEX, body=es_query)



    hits = query['aggregations']['ontvangers']['buckets']
    data = [hit for hit in hits]

    print es_query
    return json.dumps(data)