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
def table():
    return render_template('table.html')


@app.route('/viz')
def viz():
    return render_template('viz.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = SimpleSearch()
    if request.method == 'POST':
        return jsonify(form.data)
    elif request.method == 'GET':
        return render_template('form.html', form=form)


@app.route('/_ajax_streamer')
def ajax_streamer():

    values = request.args.get('search[value]')

    q_empty = {"query": {"match_all": {}}}
    q_search ={
                "query":
                    {"multi_match": {
                        "query": values,
                        "fields": ["overheid", "regeling", "ontvanger"]
                    }
                }
            }

    if values == '':
        query = q_empty
    else:
        query = q_search

    t_res = es.search(index=ES_INDEX)
    f_res = es.search(index=ES_INDEX, size=request.args.get('length'), from_=request.args.get('start'), body=query)
    records_total = t_res['hits']['total']
    records_filtered = f_res['hits']['total']
    draw = request.args.get('draw')

    hits = f_res['hits']['hits']
    data = [hit['_source'] for hit in hits]

    result = {}
    result['draw'] = draw
    result['recordsTotal'] = records_total
    result['recordsFiltered'] = records_filtered
    result['data'] = data

    print data
    return json.dumps(result)


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

    query = es.search(index=ES_INDEX, body=vaakst_uitkerende_overheden)



    hits = query['aggregations']['vaakst_uitkerende_overheden']['buckets']
    data = [hit for hit in hits]

    print data
    return json.dumps(data)