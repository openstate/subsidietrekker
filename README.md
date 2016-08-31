# Subsidietrekker
Search interface for subsidies from governments. This project is still in its development phase.
Currently being maintained by Kevin Bowey for the Open State Foundation.

#Required software
* docker-compose

#Installation
* ```cd docker```
* ```docker-compose up -d```
* ```docker exec -it docker exec -it docker_c-subsidietrekker-app_1 bash```
* ```curl -XPUT 'http://c-subsidietrekker-elasticsearch:9200/sub/' -d '@es_mapping'```
* ```cd ../app``` and create the folder ```json``` and add the json data files containing the subsidies
* ```docker exec -it docker_c-subsidietrekker-app_1 python add_subs.py```
* Go to http://<ip address of docker_c-subsidietrekker-nginx_1>/

After installation start the tool using ```docker-compose start```

#Development
Flask debug will be set to on which automatically reloads any changes made to Flask files so you don't have to restart the whole application manually
* Uncomment the `Development` sections and comment the `Production` sections in `docker/Dockerfile` and `docker/nginx-site.conf`

#Docs
* [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
* [Python](https://docs.python.org/2/)
* [Flask](http://flask.pocoo.org/docs/0.11/)
* [Elasticsearch-py module](http://elasticsearch-py.readthedocs.io/en/master/)
