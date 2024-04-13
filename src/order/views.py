from django.db.models import Max, Min
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from transliterate import translit

from account.models import User as ClassUser
from order.models import Order


User = get_user_model()


def get_data_filter_template(user: ClassUser) -> dict:
    """Отдаёт данные для фильтра шаблона."""
    user_id = None
    if user.is_authenticated:
        user_id = user.id
    users = User.objects.filter(
        id__in=Order.objects.all().values_list('user', flat=True).distinct()
        ).exclude(id=user_id)
    min_max_price = Order.objects.aggregate(Min('price'), Max('price'))
    cities = list(
        Order.objects.all().values_list('city', flat=True).distinct()
        )
    return {'users': users, 'min_max_price': min_max_price, 'cities': cities}


def get_data_filter_model(
        user: ClassUser, data: dict, data_filter_template: dict
        ) -> tuple:
    """Отдаёт данные для фильтра модели."""
    cities = data.get('cities')
    users = data.get('users')
    min_price = data.get('min_price')
    max_price = data.get('max_price')
    price = [
        data_filter_template["min_max_price"]["price__min"],
        data_filter_template["min_max_price"]["price__max"],
        ]
    if min_price and max_price:
        price = [int(min_price), int(max_price)]
    if not cities:
        cities = data_filter_template["cities"]
    else:
        cities = translit(cities, 'ru').title().split(',')
    if not users:
        users = []
        for user in data_filter_template["users"]:
            users.append(user.username)
    else:
        users = users.split(',')
    return price, cities, users


def index(request: WSGIRequest) -> HttpResponse:
    """View главной страницы."""
    user = request.user
    data_filter_template = get_data_filter_template(user)
    price, cities, users = get_data_filter_model(
        user, request.GET, data_filter_template
        )
    orders = Order.objects.filter(
        city__in=cities, user__username__in=users,
        price__range=price
        )
    if user.is_authenticated:
        orders.exclude(user=user)
    orders_сustomer = []
    orders_no_сustomer = []
    for order in orders:
        if order.is_сustomer:
            orders_сustomer.append(order)
            continue
        orders_no_сustomer.append(order)
    context = {
        'orders_сustomer': orders_сustomer,
        'orders_no_сustomer': orders_no_сustomer,
        'data_filter': data_filter_template
    }
    return render(request, 'order/index.html', context)
