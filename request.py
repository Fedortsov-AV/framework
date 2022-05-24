class Request:

    def __init__(self, environ):
        self.path_info = envirin.get('PATH_INFO')
        self.query_string = envirin.get('QUERY_STRING')
        self.addres = _get_address(environ)
        self.headers = _get_headers(environ)
        self.request_method = envirin.get('REQUEST_METHOD')
        self.request_uri = envirin.get('REQUEST_URI')
        self.script_name = envirin.get('SCRIPT_NAME')
        self.server = _get_server_info(environ)
        self.wsgi = _get_wsgi(environ)

    def _get_address(self, environ):
        addres = {}
        for key, value in environ.items():
            if key.startwith('REMOTE_'):
                addres[key[7:].lower()] = value
        return addres

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startwith('HTTP_'):
                headers[key[5:].lower()] = value
        return headers

    def _get_server_info(self, environ):
        server_info = {}
        for key, value in environ.items():
            if key.startwith('SERVER_'):
                server_info[key[7:].lower()] = value
        return server_info

    def _get_wsgi(self, environ):
        wsgi = {}
        for key, value in environ.items():
            if key.startwith('wsgi.'):
                wsgi[key[7:].lower()] = value
        return wsgi
