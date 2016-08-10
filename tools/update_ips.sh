#!/bin/bash
# Update the IPs of docker containers in python files
container=docker_c-subsidietrekker-app_1
echo "*** Retrieving IP address for $container"
ip=`docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $container`
if [[ $ip ]]
then
    echo $ip
    sed -i "s/http:\/\/[^:]*/http:\/\/$ip/g" ../app/static/scripts/datatables_script.js
    sed -i "s/http:\/\/[^:]*/http:\/\/$ip/g" ../app/static/scripts/d3_script.js
fi  

container=docker_c-subsidietrekker-elasticsearch_1
echo "*** Retrieving IP address for $container"
ip=`docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $container`
if [[ $ip ]]
then
    echo $ip
    sed -i "s/http:\/\/[^:]*/http:\/\/$ip/g" ../app/app.py
    sed -i "s/http:\/\/[^:]*/http:\/\/$ip/g" ../app/add_subs.py
fi  
