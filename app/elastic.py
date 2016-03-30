'''
Subsidietrekker.nl

Elastic.py

'''
from elasticsearch import Elasticsearch

ES_CLUSTER = 'http://localhost:9200'
ES_INDEX = 'sub'
ES_TYPE = 'item'
es = Elasticsearch(ES_CLUSTER)

# zoekterm='', overheid='false', ontvanger='false', regeling='false', beleidsartikel='false', query_type='simple', table='false', viz='false', raw='false'
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
    fields = list()
    if form_data['overheid'] == 'true':
        fields.append('overheid')
    if form_data['ontvanger'] == 'true':
        fields.append('ontvanger')
    if form_data['regeling'] == 'true':
        fields.append('regeling')
    if form_data['beleidsartikel'] == 'true':
        fields.append('beleidsartikel')
    form_dict['fields'] = fields
    data_dict['form'] = form_dict

    return data_dict



def query_builder(cleaned_data):
    ''' build ES query using cleaned data from receiver '''
    # if cleaned_data['settings']['query_type'] == 'simple':
    #     base = simple_base
    # elif cleaned_data['settings']['query_type'] == 'compare':
    #     base = compare_base


    base = { "query": cleaned_data['form_dict']['zoekterm']}





def query_es(query_data):
    ''' query ES '''
    pass


def pass_to_table(query_results):
    ''' pass query results to datatables '''
    pass


def pass_to_viz(query_results):
    ''' pass query results to d3 '''
    pass