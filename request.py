class Request:

    def __init__(self, environ):
        self.path_info = environ.get('PATH_INFO')
        self.query_string = self._get_query_string(environ)
        self.addres = self._get_address(environ)
        self.headers = self._get_headers(environ)
        self.request_method = environ.get('REQUEST_METHOD')
        self.request_uri = environ.get('REQUEST_URI')
        self.script_name = environ.get('SCRIPT_NAME')
        self.server = self._get_server_info(environ)
        self.wsgi = self._get_wsgi(environ)

    def _get_query_string(self, environ):
        query = {}
        query_string = environ.get('QUERY_STRING')
        if query_string:
            for _ in ['/', '&', ' ']:
                if query_string.endswith(_):
                    print(f'_ {_} -> {query_string[-1]}')
                    query_string = query_string[:-1]

            for _ in ['%20', ]:
                if query_string.endswith(_):
                    query_string = query_string[:-3]

            query_list = query_string.split("&")

            for query_item in query_list:
                index = query_item.find('=')
                query[query_item[:index]] = query_item[index + 1:]
            print(query)
            return query
        return {}

    def _get_address(self, environ):
        addres = {}
        for key, value in environ.items():
            if key.startswith('REMOTE_'):
                addres[key[7:].lower()] = value
        return addres

    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value
        return headers

    def _get_server_info(self, environ):
        server_info = {}
        for key, value in environ.items():
            if key.startswith('SERVER_'):
                server_info[key[7:].lower()] = value
        return server_info

    def _get_wsgi(self, environ):
        wsgi = {}
        for key, value in environ.items():
            if key.startswith('wsgi.'):
                wsgi[key[7:].lower()] = value
        return wsgi
