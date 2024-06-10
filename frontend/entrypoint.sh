#!/bin/bash

#Wait API is Ready!
until curl --output /dev/null --silent --head --fail $API_URL; do
    sleep 1
done

pip3 install -r /app/requirements.txt
flask run --host=0.0.0.0 --port 8080
tail -f /dev/null