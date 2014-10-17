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

from django.http import HttpResponse


def html_message(request):
    return HttpResponse(HTML_MESSAGE, content_type="text/html")

def short_message(request):
    return HttpResponse(SHORT_MESSAGE, content_type="text/plain")

def average_message(request):
    return HttpResponse(AVERAGE_MESSAGE, content_type="text/plain")

def long_message(request):
    return HttpResponse(LONG_MESSAGE, content_type="text/plain")

def json_message(request):
    return HttpResponse(json.dumps(JSON_MESSAGE), content_type='application/json')

def slow_request(request):
    SLOW_REQUEST()
    return HttpResponse(SLOW_MESSAGE, content_type="text/plain")
