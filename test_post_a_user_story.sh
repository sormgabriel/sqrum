#!/bin/bash


curl -i -H "Content-Type: application/json" -X POST -d '{"id":/$1/,"rol":"como tu vieja","description":"quiero cagarte a golpes"}' http://localhost:5000/sqrum/api/v1.0/userstories

#curl -i -H "Content-type: application/json" -X POST -d '{"rol":"Como desarrollador","description":"quiero ver todas las user stories"}' http://localhost:5000/sqrum/api/v1.0/userstories


