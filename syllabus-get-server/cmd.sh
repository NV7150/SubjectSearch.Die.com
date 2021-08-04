#!/bin/bash
set -e

until psql -h "db" -U $POSTGRES_USER -d $POSTGRES_DB -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

exec python3 main.py