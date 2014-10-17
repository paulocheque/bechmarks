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

from bottle import route, run, response


@route('/short-message')
def short_message():
    response.content_type = 'text/plain'
    return SHORT_MESSAGE


@route('/average-message')
def average_message():
    response.content_type = 'text/plain'
    return AVERAGE_MESSAGE


@route('/long-message')
def long_message():
    response.content_type = 'text/plain'
    return LONG_MESSAGE


@route('/slow-request')
def slow_request():
    response.content_type = 'text/plain'
    SLOW_REQUEST()
    return SLOW_MESSAGE


@route('/json-message')
def json_message():
    response.content_type = 'application/json'
    return json.dumps(JSON_MESSAGE)


@route('/')
def json_message():
    response.content_type = 'text/html'
    return HTML_MESSAGE



if __name__ == "__main__":
    import os
    server = os.getenv('SERVER', None)
    port = int(os.environ.get('PORT', 9999))
    if server:
        run(host='0.0.0.0', port=port, server=server)
    else:
        run(host='0.0.0.0', port=port)


# GUNICORN

# import multiprocessing
# import os
# import sys

# _is_pypy = hasattr(sys, 'pypy_version_info')
# _is_travis = os.environ.get('TRAVIS') == 'true'

# workers = multiprocessing.cpu_count() * 3
# if _is_travis:
#     workers = 2

# bind = "0.0.0.0:8080"
# keepalive = 120
# errorlog = '-'
# pidfile = 'gunicorn.pid'

# if _is_pypy:
#     worker_class = "tornado"
# else:
#     worker_class = "meinheld.gmeinheld.MeinheldWorker"

#     def post_fork(server, worker):
#         # Disable access log.
#         # (Until https://github.com/mopemope/meinheld/pull/42 is released)
#         import meinheld.server
#         meinheld.server.set_access_logger(None)



# setup

# import os
# import subprocess

# CWD = os.path.dirname(__file__)


# def start(args, logfile, errfile):
#     subprocess.Popen(
#         "$PY2_GUNICORN app:app -c gunicorn_conf.py",
#         cwd=CWD, stderr=errfile, stdout=logfile, shell=True)
#     return 0


# def stop(logfile, errfile):
#     subprocess.call(
#         "kill `cat gunicorn.pid`",
#         cwd=CWD, stderr=errfile, stdout=logfile, shell=True)
#     return 0



# nginx uwsgi

# import subprocess
# import multiprocessing
# import os


# CWD = os.path.abspath(os.path.dirname(__file__))
# bin_dir = os.path.expandvars('$PY2_ROOT/bin')
# NCPU = multiprocessing.cpu_count()
# NGINX_COMMAND = 'sudo /usr/local/nginx/sbin/nginx -c ' + CWD + '/nginx.conf'


# def start(args, logfile, errfile):
#     try:
#         subprocess.call(
#             NGINX_COMMAND,
#             shell=True, stdout=logfile, stderr=errfile)

#         # Run in the background, but keep stdout/stderr for easy debugging
#         subprocess.Popen(
#             "{0}/uwsgi --ini uwsgi.ini --processes {1} --wsgi app:app".format(
#                 bin_dir, NCPU*3),
#             shell=True, cwd=CWD, stderr=errfile, stdout=logfile)
#         return 0
#     except subprocess.CalledProcessError:
#         return 1


# def stop(logfile, errfile):
#     subprocess.call(
#         NGINX_COMMAND + ' -s stop',
#         shell=True, stdout=logfile, stderr=errfile)

#     subprocess.call(bin_dir + '/uwsgi --stop /tmp/uwsgi.pid',
#                     shell=True, stderr=errfile, stdout=logfile)
#     return 0



# import subprocess


# def start(args, logfile, errfile):
#     subprocess.Popen(
#         "$PY2_GUNICORN --pid=gunicorn.pid hello.wsgi:application -c gunicorn_conf.py --env DJANGO_DB=mysql",
#         cwd="django", shell=True, stderr=errfile, stdout=logfile)
#     return 0


# def stop(logfile, errfile):
#     subprocess.call(
#         "kill `cat gunicorn.pid`",
#         cwd="django", shell=True, stderr=errfile, stdout=logfile)
#     return 0