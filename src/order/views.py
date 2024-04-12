from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render

from order.models import Order


def index(request):
    """View главной страницы."""
    orders_сustomer = Order.objects.filter(is_сustomer=True)
    orders_no_сustomer = Order.objects.filter(is_сustomer=False)
    if not isinstance(request.user, AnonymousUser):
        orders_сustomer = orders_сustomer.exclude(user=request.user)
        orders_no_сustomer = orders_no_сustomer.exclude(user=request.user)
    context = {
        'orders_сustomer': orders_сustomer,
        'orders_no_сustomer': orders_no_сustomer,
    }
    return render(request, 'order/index.html', context)
