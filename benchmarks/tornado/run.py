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

import tornado.ioloop
import tornado.web

class HtmlHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/html")
        self.write(HTML_MESSAGE)

class ShortMessageHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/plain")
        self.write(SHORT_MESSAGE)

application = tornado.web.Application([
    (r"/", HtmlHandler),
    (r"/short-message", ShortMessageHandler),
])

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 9999))

    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
