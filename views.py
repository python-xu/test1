from django.http import HTTPResponse


def index(request):
    return HttpResponse('index')
