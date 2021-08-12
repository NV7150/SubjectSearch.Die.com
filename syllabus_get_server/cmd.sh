#!/bin/bash
set -e

until psql -h "db" -U $POSTGRES_USER -d $POSTGRES_DB -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

if test $TEST -eq 1 ; then
  exec python3 test/unittester.py
else
  exec python3 syllabus_get_server/main.py
fi
