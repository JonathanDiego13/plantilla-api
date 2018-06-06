import os
import multiprocessing


# server socket
bind = '0.0.0.0:8001'  # socket to bind to
backlog = 2048  # Number of pending connections. max waiting clients

# worker processes
# number of workers processes that this server should keep alive
workers = 2 * multiprocessing.cpu_count() + 1
worker_class = 'gevent'  # worker to use
# for gevent - max simultaneous connections that a single process can handle
worker_connections = 1000
timeout = 60  # max seconds to process a single request
keepalive = 5  # number of seconds to wait for hte next request on a keep-alive http connection

# Logging
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
errorlog = os.path.join(parent_dir, 'logs/gunicorn.error.logs')
accesslog = os.path.join(parent_dir, 'logs/gunicorn.access.logs')  # file to write access log to.
loglevel = 'debug'

"""
HOST, USER, DATE, STATUS_LINE, REQUEST_METHOD, URL, QUERY, PROTOCOL, STATUS, RESPONSE_LENGTH, 
REQUEST_TIME_DECIMAL_SECONDS, 
"""
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(m)s %(U)s %(q)s %(H)s %(s)s %(B)s %(L)s'
