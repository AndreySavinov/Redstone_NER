#!/usr/bin/env python
# coding: utf-8

"""
Very simple HTTP server in python for detection 
of ORG entites via spacy model
Usage::
    python3 server_aws.py [<port>]
    
    OR
    
    nohup python3 server_aws.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import spacy

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write(str("Hi, server is running").encode('utf-8'))
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) # processing of text from obtained json
        text = post_data.decode('utf-8').split(':')[1]
        text = text.replace('}', '')
        text = text[2:-1]
        str_for_spacy = str(text)
        response = []
        doc = nlp(str_for_spacy)
        for entity in doc.ents:
            if entity.label_ == 'ORG':
                response.append((entity.text, entity.label_))
        self._set_response()
        self.wfile.write(str(response).format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    global nlp
    nlp = spacy.load("en_core_web_sm")
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

