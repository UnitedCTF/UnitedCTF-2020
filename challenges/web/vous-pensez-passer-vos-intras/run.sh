#!/bin/bash

service mysql start
mysql < create_db.sql
rm create_db.sql
mvn clean spring-boot:run 
