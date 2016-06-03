# subsidietrekker
README.md for the Subsidietrekker.nl web application. This project is still in its development phase. 
Currently being maintained by Kevin Bowey for the Open State Foundation.


#Required software
ElasticSearch 2.0+

Python2.7+

Required modules: Flask, requests, elasticsearch-py

(Pip freeze readout:
dominate==2.2.0
elasticsearch==2.3.0
Flask==0.10.1
Flask-WTF==0.12
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
requests==2.9.1
urllib3==1.14
visitor==0.1.2
Werkzeug==0.11.4
WTForms==2.1)

#Installation
1. Install ElasticSearch
2. Put the ES mappings found @ /subsidietrekker/tools/es_mapping in the /sub/ index through a put request
3. Create a virtual environment and install the required python modules ontop of it.
4. Activate the venv and start the flask development server with "python PATH/app/main.py"
5. The subsidietrekker dev server should now run @ http://localhost:5000/

#Docs
ElasticSearch: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

Python: https://docs.python.org/2/

Flask: http://flask.pocoo.org/docs/0.11/

Elasticsearch-py module: http://elasticsearch-py.readthedocs.io/en/master/
