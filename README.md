# subsidietrekker
Search interface for subsidies from governments. This project is still in its development phase. 
Currently being maintained by Kevin Bowey for the Open State Foundation.


#Required software
* Docker

#Installation
1. ```cd docker```
2. ```docker-compose up -d```
4. ```curl -XPUT 'http://<ip address of docker_c-subsidietrekker-elasticsearch_1>:9200/sub/' -d '@tools/es_mapping'```
5. ```cd tools```
5. ```python add_subs.py```
7. ```# goto http://<ip address of docker_c-subsidietrekker-nginx_1>/```

#Docs
* [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
* [Python](https://docs.python.org/2/)
* [Flask](http://flask.pocoo.org/docs/0.11/)
* [Elasticsearch-py module](http://elasticsearch-py.readthedocs.io/en/master/)
