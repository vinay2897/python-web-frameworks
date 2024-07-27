from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world 1. You're at the polls index.")