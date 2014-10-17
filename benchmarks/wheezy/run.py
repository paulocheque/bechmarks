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

from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.http import bootstrap_http_defaults
from wheezy.http import not_found


def html_message(request):
    response = HTTPResponse()
    response.write(HTML_MESSAGE)
    return response

def short_message(request):
    response = HTTPResponse()
    response.write(SHORT_MESSAGE)
    return response

def average_message(request):
    response = HTTPResponse()
    response.write(AVERAGE_MESSAGE)
    return response

def long_message(request):
    response = HTTPResponse()
    response.write(LONG_MESSAGE)
    return response

def json_message(request):
    response = HTTPResponse()
    response.write(json.dumps(JSON_MESSAGE))
    return response

def slow_request(request):
    SLOW_REQUEST()
    response = HTTPResponse()
    response.write(SLOW_MESSAGE)
    return response


def router_middleware(request, following):
    path = request.path
    if path == '/':
        response = html_message(request)
    elif path == '/short-message':
        response = short_message(request)
    elif path == '/average-message':
        response = average_message(request)
    elif path == '/long-message':
        response = long_message(request)
    elif path == '/json-message':
        response = json_message(request)
    elif path == '/slow-request':
        response = slow_request(request)
    else:
        response = not_found()
    return response


options = {}
main = WSGIApplication([
    bootstrap_http_defaults,
    lambda ignore: router_middleware
], options)


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 9999))
    from wsgiref.simple_server import make_server
    try:
        make_server('', port, main).serve_forever()
    except KeyboardInterrupt:
        pass
