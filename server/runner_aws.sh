#!/usr/bin/env bash

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
sudo yum install git
pip install -U spacy
python3 -m spacy download en_core_web_sm


