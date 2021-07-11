#!/usr/bin/env python3
"""
Very simple HTTP server in python for detection 
of ORG entites via pretrained BERT

https://github.com/kamalkraj/BERT-NER/ - source code of BERT

https://onedrive.live.com/?authkey=%21AG6vMTjttNHJR5E&cid=390AF7A51B5537E7&id=390AF7A51B5537E7%21776&parId=390AF7A51B5537E7%21775&action=locate/ - pretrained model

Usage::   
    python3 server_bert.py [<port>]
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import os


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
        str_for_bert = str(text)
        output = bert.predict(str_for_bert)
        response = []
        for item in output:
            if item['tag'] == 'B-ORG' or item['tag'] == 'I-ORG':
                response.append((item['word'], item['tag'], item['confidence']))
        self._set_response()
        self.wfile.write(str(response).format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=80, 
        path_to_out_base = "out_base/", folder_with_bert_py = "BERT-NER"):
    global bert
    bert = make_model(path_to_out_base, folder_with_bert_py)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    
def make_model(path_to_out_base = "out_base/", folder_with_bert_py = "BERT-NER"):
    cwd=os.getcwd()
    os.chdir(folder_with_bert_py)
    from bert import Ner
    model = Ner("out_base/")
    os.chdir(cwd)
    return model

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()