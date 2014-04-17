# Set the path
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gevent.wsgi import WSGIServer
from salebadger import app

http_server = WSGIServer(('', 80), app)

if __name__ == "__main__":
    http_server.serve_forever()
