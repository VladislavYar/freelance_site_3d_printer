from django.contrib import admin

from order.models import Order, OrderImage


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderImage)
class OrderImagesAdmin(admin.ModelAdmin):
    pass
