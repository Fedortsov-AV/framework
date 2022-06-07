class Response:
    def __init__(self, body: str, status: str = None, headers=None):
        self.body = body
        self.headers = self.add_headers(headers)
        self.status = status

    @staticmethod
    def add_headers(add_headers):
        headers = {
            'Content-Type': 'text/html'
        }
        if add_headers:
            headers.update(add_headers)
        return headers
