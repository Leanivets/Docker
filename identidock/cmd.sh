#!/bin/bash

set -e

if [ "$ENV" = 'DEV' ]
then
	echo "Run DEV"
	exec python3 "identidock.py"
else
	echo "Run product"
	exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py --callable app --stats 0.0.0.0:9191
fi
