import pprint


def app(environ, start_response):
    pprint.pprint(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Well nice']