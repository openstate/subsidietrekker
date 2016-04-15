'''
Subsidietrekker.nl

views.py

'''

from flask import render_template, request, jsonify
import json

from app import app
from elastic import *
from forms import SimpleSearch

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo')#, methods=['GET', 'POST'])
def demo():
    # form = SimpleSearch()
    # if request.method == 'POST':
    #     print form.data
    #     return json.dumps(receiver(**form.data))
    # elif request.method == 'GET':
    return render_template('demo.html')#, form=form)

@app.route('/data')
def over_data():
    return render_template('over_data.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/viz')
def viz():
    return render_template('viz.html')

#     form = SimpleSearch()
#     if request.method == 'POST':
#         print form.data
#         return json.dumps(receiver(**form.data))
#     elif request.method == 'GET':
#         return render_template('form.html', form=form)

# The new steamer function WIP
@app.route('/_streamer')
def streamer():

    da_dump = {}

    def datatables_streamer():

        search = request.args.get('search[value]')
        #fields = request.args.get('buttons')
        draw = request.args.get('draw')
        result = {}


        es_query = {
                        "query": {
                            "simple_query_string": {
                                "query": search,
                                "analyzer": "snowball",
                                "fields": ['_all'], #fields,
                                "default_operator": "and"
                            }
                        }
                    }


        if search == '':
            query = es.search(index=ES_INDEX)
        else:
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

    da_dump = datatables_streamer()
    #da_dump['datatables'] = datatables_streamer()
    #da_dump['d3'] = d3_streamer()

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

    print data
    return json.dumps(data)