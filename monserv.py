#!/usr/bin/python3
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler,HTTPServer
from jinja2 import Environment, PackageLoader, select_autoescape,FileSystemLoader
import os

def getStat(stat):
    f=open('./templates'+stat)
    lr=f.read()
    f.close()
    return lr
def getHTML(myvar):
    #env = Environment() 
    #loader=PackageLoader('monserv', 'templates'),
    #autoescape=select_autoescape(['html', 'xml'])
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader = FileSystemLoader(template_dir), autoescape = True)
    template = env.get_template('base.html')
    return  template.render(myvar)

    
class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        sl={}
        if self.path in ['/css/bootstrap.min.css','/js/jquery-3.2.1.slim.min.js','/js/tether.min.js','/js/bootstrap.min.js']:
           lr=getStat(self.path) 
           print (lr)
           self.wfile.write(bytes(lr,"utf-8"))
        else:
           self.wfile.write(bytes(getHTML(sl)+self.path,"utf-8"))
          
def main ():
    serv = HTTPServer(("localhost",8888),HttpProcessor)
    serv.serve_forever()


 
if __name__ == "__main__":
    main()