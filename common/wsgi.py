from common.request import Request
from urls import urls
from view import not_url


def app(environ, start_response):
    request = Request(environ)
    response = None
    for url in urls:
        if url.path == request.path:
            response = url.view(request)
            break
        response = not_url(request)
    start_response(response.status, [(key, value) for key, value in response.headers.items()])

    return [response.body.encode('UTF-8')]
