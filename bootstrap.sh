#!/bin/bash

python3 -m venv venv
echo 'Create virtualenv.'

source $PWD/venv/bin/activate

python3 -m pip install -r requirements.txt

echo 'Project initialization is complete!'

echo 'Start the demo：'

python3 manage.py runserver 8000