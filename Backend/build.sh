#!/usr/bin/env bash
set -o errexit
pip install -r req.txt
python manage.py collectstatic --noinput
python manage.py migrate