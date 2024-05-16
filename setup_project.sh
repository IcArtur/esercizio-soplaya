#!/bin/bash

echo "Executing basic command to make the project work."

pip3 install -r requirements.txt
python3 soplaya_exercise/manage.py migrate

echo "Package installation and migrations are done, you can now freely use the project."