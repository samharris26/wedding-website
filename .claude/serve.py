import os, sys
site = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(site)
from http.server import HTTPServer, SimpleHTTPRequestHandler
HTTPServer(("127.0.0.1", 8642), SimpleHTTPRequestHandler).serve_forever()
