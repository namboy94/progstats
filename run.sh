#!/bin/bash

export FLASK_APP=progstats/router.py
export PROGSTATS_DATA="$(pwd)/data"
flask run