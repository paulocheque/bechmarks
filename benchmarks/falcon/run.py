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

import falcon

class HtmlMessage(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', 'text/html')
        response.body = HTML_MESSAGE


class ShortMessage(object):
    def on_get(self, request, response):
        response.set_header('Content-Type', 'text/plain')
        response.body = SHORT_MESSAGE



app = falcon.API()
app.add_route("/", HtmlMessage())
app.add_route("/short-message", ShortMessage())


if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 9999))

    from wsgiref import simple_server

    httpd = simple_server.make_server('localhost', port, app)
    httpd.serve_forever()
