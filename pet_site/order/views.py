from django.shortcuts import render


def index(request):
    """View главной страницы."""
    return render(request, 'order/index.html')
