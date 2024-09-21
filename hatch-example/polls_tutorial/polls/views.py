from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world (from Hatch-example). You're at the polls index.")
