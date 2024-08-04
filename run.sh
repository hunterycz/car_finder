#!/bin/bash

# Run the Flask app
python server.py

# To ensure the script doesn't close the pipenv shell immediately after the command
exec $SHELL
