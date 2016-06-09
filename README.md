# subsidietrekker
Search interface for subsidies from governments. This project is still in its development phase. 
Currently being maintained by Kevin Bowey for the Open State Foundation.


#Required software

* ElasticSearch 2.0+ ([2.3.3](https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.3/elasticsearch-2.3.3.tar.gz))
* Python2.7+

#Installation

1. Make sure Elasticsearch is installed and running
2. ```virtualenv --no-site-packages .venv```
3. ```pip install -r requirements.txt````
4. ```curl -XPUT 'http://localhost:9200/sub/' -d '@tools/es_mapping'```
5. ```./app/main.py```
6. ```# goto http://localhost:5000/``` 

#Docs

* [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
* [Python](https://docs.python.org/2/)
* [Flask](http://flask.pocoo.org/docs/0.11/)
* [Elasticsearch-py module](http://elasticsearch-py.readthedocs.io/en/master/)
