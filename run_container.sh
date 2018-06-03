#!/bin/bash

docker run -v "$(pwd)":/opt/test_flask_01 --network host --name test-flask-01 test-flask-01 flask run

