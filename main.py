from waitress import serve
from wsgi import app

if __name__ == "__main__":
    serve(app, host="localhost", port=8000)