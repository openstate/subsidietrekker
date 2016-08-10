# Subsidietrekker
Search interface for subsidies from governments. This project is still in its development phase. 
Currently being maintained by Kevin Bowey for the Open State Foundation.

#Required software
* Docker

#Installation
* ```cd docker```
* ```docker-compose up -d```
* ```cd ../tools```
* ```./update_ips.sh```
* ```curl -XPUT 'http://<ip address of docker_c-subsidietrekker-elasticsearch_1>:9200/sub/' -d '@es_mapping'```
* ```cd ../app``` and create the folder ```json``` and add the json data files containing the subsidies
* ```docker exec -it docker_c-subsidietrekker-app_1 python add_subs.py```
* Go to http://<ip address of docker_c-subsidietrekker-nginx_1>/

#Docs
* [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
* [Python](https://docs.python.org/2/)
* [Flask](http://flask.pocoo.org/docs/0.11/)
* [Elasticsearch-py module](http://elasticsearch-py.readthedocs.io/en/master/)
