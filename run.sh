#!/usr/bin/env bash

# need python3.7+ installed

python3 -m venv venv/
pip install -r requirements.txt
sudo ./venv/bin/python3 main.py