#!/bin/bash

flask db upgrade
exec "$@"
gunicorn -c "guinicorn.conf.py" "app:create_app()"