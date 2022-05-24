import pprint


def app(environ, start_response):
    pprint.pprint(environ.get('wsgi.input').read())
    start_response('200 OK', [('Content-Type', 'text/html')])
    print('*'*50)
    return [b'Well nice']