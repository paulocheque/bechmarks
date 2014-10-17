#!/usr/bin/env python

import json
import time

SHORT_MESSAGE = '0123456789' * 100 # ~1kb
AVERAGE_MESSAGE = '0123456789' * 10000 # ~100kb
LONG_MESSAGE = '0123456789' * 100000 # ~1mb
JSON_MESSAGE = {}
SLOW_REQUEST = lambda: time.sleep(1) # seconds
SLOW_MESSAGE = 'slow request'
HTML_MESSAGE = '''
<ul>
    <li><a href="/short-message">short-message</a></li>
    <li><a href="/average-message">average-message</a></li>
    <li><a href="/long-message">long-message</a></li>
    <li><a href="/slow-request">slow-request</a></li>
    <li><a href="/json-message">json-message</a></li>
</ul>
'''

import fapws._evwsgi as evwsgi
from fapws import base

def start():
    import os
    port = int(os.environ.get('PORT', 9999))
    evwsgi.start('0.0.0.0', port)
    evwsgi.set_base_module(base)

    def html_message(environ, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return ['hello world!!']

    def short_message(environ, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return ['hello world!!']

    def average_message(environ, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return ['hello world!!']

    def long_message(environ, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return ['hello world!!']

    def json_message(environ, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return ['hello world!!']

    def slow_request(environ, start_response):
        start_response('200 OK', [('Content-Type','text/html')])
        return ['hello world!!']

    evwsgi.wsgi_cb(('/', html_message))
    evwsgi.wsgi_cb(('/short-message', short_message))
    evwsgi.wsgi_cb(('/average-message', average_message))
    evwsgi.wsgi_cb(('/long-message', long_message))
    evwsgi.wsgi_cb(('/json-message', json_message))
    evwsgi.wsgi_cb(('/slow-request', slow_request))

    evwsgi.set_debug(0)
    evwsgi.run()

if __name__ == '__main__':
    start()