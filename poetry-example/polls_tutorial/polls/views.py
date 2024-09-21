from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world (from Poetry-example). You're at the polls index.")
