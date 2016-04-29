'''

Subsidietrekker.nl

streamer.py

'''

import json

from app import app
from elastic import *


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

        search = request.args.get('search[value]')
        #fields = request.args.get('buttons')
        draw = request.args.get('draw')
        sort = request.args.get('order[0][dir]')
        result = {}


        es_query = {
                        "query": {
                            "simple_query_string": {
                                "query": search,
                                "analyzer": "snowball",
                                "fields": ['_all'], #fields,
                                "default_operator": "and"
                            }
                        },
                        "sort": {"overheid": {"order": sort}}
                    }


        # if search == '':
        #     query = es.search(index=ES_INDEX)
        # else:
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
    # test = [{'overheid': 1, 'realisatie': 34}, {'overheid': 1, 'realisatie': 34}, {'overheid': 1, 'realisatie': 34}]

    # ontvanger
    top10 = {
                "filter" : {
                    "match_all" : { }
                },
                "sort": [
                    {
                        "realisatie": {
                            "order": "desc"
                        }
                }
                ],
                "size": 10
            }

    afzonderlijke_subsidie_ontvangers = {
        "size": 0,
        "aggs": {
            "afzonderlijke_subsidie_ontvangers": {
                "terms": {
                    "field": "ontvanger.raw"
                }
            }
        }
    }

    # overheid
    vaakst_uitkerende_overheden = {
        "aggs": {
            "vaakst_uitkerende_overheden": {
                "terms": {
                    "field": "overheid.raw"
                }
            }
        }
    }

    # regeling
    meest_gebruikte_regeling = {
        "aggs": {
            "meest_gebruikte_regeling": {
                "terms": {
                    "field": "regeling.raw"
                }
            }
        }
    }

    query = es.search(index=ES_INDEX, body=afzonderlijke_subsidie_ontvangers)



    hits = query['aggregations']['afzonderlijke_subsidie_ontvangers']['buckets']
    data = [hit for hit in hits]

    # print data
    return json.dumps(data)