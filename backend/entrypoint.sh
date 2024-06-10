#!/bin/bash

#Wait MySql is Ready!
while ! mysqladmin ping -h"$MYSQL_HOST" -uroot -p"$MYSQL_ROOT_PASSWORD" --silent; do
    sleep 1
done

pip3 install -r /app/requirements.txt
flask run --host=0.0.0.0 --port 8080
tail -f /dev/null