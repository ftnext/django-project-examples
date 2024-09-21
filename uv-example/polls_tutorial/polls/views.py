from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world (from uv-example). You're at the polls index.")
