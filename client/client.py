#!/usr/bin/env python3
"""
Very simple HTTP client in python for detection 
of ORG entites via pretrained BERT or spacy model

Usage::   
    python3 client.py 'text to be processed' 'url of server'
    
    or from IPython notebook as is demo_client.ipynb
"""


import requests

def request_GET(URL = "http://3.68.101.138:8080/"):
    r = requests.get(url=URL)
    print(r.text)
    
def request_POST(message, URL = "http://3.68.101.138:8080/"):
    r = requests.post(url = URL, json={"paragraph": message})
    for item in r.text[1:-2].split('),'):
        print(item.replace('(', ''))
        
if __name__ == '__main__': 
    from sys import argv
    if len(argv) == 2:
        request_GET()
        request_POST(str(argv[1]))
    elif len(argv)==3:
        request_GET(URL = str(argv[2]))
        request_POST(str(argv[1]))
    else:
        request_GET()
        request_POST('Steve works in EU for British Petroleum', URL = "http://3.68.101.138:8080/")