''' 

Subsidietrekker.nl

add_subs.py



'''

import os
import json
from elasticsearch import Elasticsearch, helpers

# ElasticSearch config info
ES_CLUSTER = 'http://localhost:9200'
ES_INDEX = '13juli'
ES_TYPE = 'item'
es = Elasticsearch(ES_CLUSTER)


data = []
new_data = []
bulk_data = []

# Open .json files in /json, load items as values in temp_item dict, append dicts to new_data list
for filename in os.listdir(os.getcwd() + '/json/'):
    if filename.endswith('.json'):
        with open(filename) as f:
            data = json.load(f)
        for item in data['rows']:
            temp_item = {}
            temp_item['overheid'] = item[0]
            temp_item['regeling'] = item[1]
            temp_item['ontvanger'] = item[2]
            temp_item['beleid'] = item[3]
            temp_item['realisatie'] = item[4]
            temp_item['jaar'] = item[5]
            new_data.append(temp_item)

# Load new_data dicts as _source values in temp_bulk_item dicts, append temp dicts to bulk_data list
for item in new_data:
    temp_bulk_item = {}
    temp_bulk_item['_index'] = ES_INDEX
    temp_bulk_item['_type'] = ES_TYPE
    temp_bulk_item['_source'] = item
    bulk_data.append(temp_bulk_item)

# Use bulk helper function to index bulk_data dicts in ElasticSearch
helpers.bulk(client=es, actions=bulk_data)