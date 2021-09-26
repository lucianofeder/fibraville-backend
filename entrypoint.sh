#!/bin/sh

flask db migrate

exec "$@"