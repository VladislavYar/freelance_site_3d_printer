from django.db import transaction
from django.db.models import Max, Min
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from transliterate import translit

from account.models import User as ClassUser
from order.constants import ORDERS_PRE_PAGE
from order.forms import OrderForm
from order.models import Order, OrderImage


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


def get_pagination(
        orders_no_customer: list, orders_customer: list, data_get: dict
        ) -> tuple[Paginator]:
    """Отдаёт пагинацию заказов/предложений."""
    orders_no_customer_paginator = Paginator(
        orders_no_customer, ORDERS_PRE_PAGE
        )
    orders_customer_paginator = Paginator(orders_customer, ORDERS_PRE_PAGE)
    page_customer = data_get.pop('page_customer', ['1'])[0]
    page_no_customer = data_get.pop('page_no_customer', ['1'])[0]
    page_obj_customer = orders_customer_paginator.get_page(page_customer)
    page_obj_no_customer = orders_no_customer_paginator.get_page(
        page_no_customer
    )
    return page_obj_customer, page_obj_no_customer


def get_filter_orders(
        user: ClassUser, cities: list, users: list, price: list
        ) -> tuple[list[Order]]:
    """Отдаёт отфильтрованные заказы/предложения."""
    orders = Order.objects.filter(
        city__in=cities, user__username__in=users,
        price__range=price
        )
    if user.is_authenticated:
        orders.exclude(user=user)
    orders_customer = []
    orders_no_customer = []
    for order in orders:
        if order.is_customer:
            orders_customer.append(order)
            continue
        orders_no_customer.append(order)
    return orders_customer, orders_no_customer


def save_order(
        form: OrderForm, user: ClassUser, images: list | None
        ) -> None:
    """Сохраняет заказ/предложение."""
    order = form.save(commit=False)
    order.user_id = user.id
    order.save()
    if images:
        with transaction.atomic():
            for image in images:
                OrderImage(order=order, image=image).save()


def index(request: WSGIRequest) -> HttpResponse:
    """View главной страницы."""
    user = request.user
    data_get = request.GET.copy()
    data_filter_template = get_data_filter_template(user)
    price, cities, users = get_data_filter_model(
        user, data_get, data_filter_template
        )
    orders_customer, orders_no_customer = get_filter_orders(
        user, cities, users, price
        )
    page_obj_customer, page_obj_no_customer = get_pagination(
        orders_no_customer, orders_customer, data_get
        )
    form = OrderForm()
    form_valid = True
    if request.method == 'POST' and user.is_authenticated:
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            save_order(form, user, request.FILES.getlist('images'))
            return redirect('order:index')
        form_valid = False

    customer_tab = data_get.pop('customer_tab', ['1'])[0]
    request.GET = data_get
    context = {
        'orders_customer': page_obj_customer,
        'orders_no_customer': page_obj_no_customer,
        'data_filter': data_filter_template,
        'customer_tab': customer_tab,
        'form': form,
        'form_valid': form_valid,
    }
    return render(request, 'order/index.html', context)
