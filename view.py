from common.render import render
from common.response import Response


def index(request):
    return Response(render('index.html'), '200 OK')


def about(request):
    return Response(render('about.html'), '200 OK')


def not_url(request):
    return Response(render('404.html'), '404')
