# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:57:28 2019

@author: dv.zhilenkov
"""

from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()