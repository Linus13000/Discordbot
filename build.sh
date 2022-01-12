#!/bin/bash
python -m venv venv
source venv/bin/activate
venv/bin/python -m pip install --upgrade pip
pip install -r requirements.txt
