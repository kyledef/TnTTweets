#!/bin/bash

DIRECTORY="venv"

if [ ! -d "$DIRECTORY" ]; then
	echo "Setup virtualenv for current folder"
	virtualenv venv
	source venv/bin/activate
	echo "Installing requirements from requirements.txt"
	pip install -r requirements.txt
fi