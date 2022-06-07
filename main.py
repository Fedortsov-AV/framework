from waitress import serve
from common.wsgi import app

if __name__ == "__main__":
    serve(app, host="localhost", port=8035)