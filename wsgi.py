import pprint
from request import Request


def app(environ, start_response):
    request = Request(environ)
    pprint.pprint(request.query_string)
    start_response('200 OK', [('Content-Type', 'text/html')])
    print('*'*50)
    return [b'Well nice']