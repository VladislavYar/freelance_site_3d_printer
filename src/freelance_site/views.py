from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http.response import Http404


def about(request: WSGIRequest) -> HttpResponse:
    """View о создателе."""
    return render(request, "freelance_site/about.html")


def page_404(request: WSGIRequest, exception: Http404) -> HttpResponse:
    """View 404."""
    return render(request, "freelance_site/404.html")
