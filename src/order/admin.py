from django.contrib import admin

from order.models import Order, OrderImage, Locality


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'is_customer',
        'description',
        'price',
        'locality',
        'date',
    )
    readonly_fields = ('locality', )


@admin.register(OrderImage)
class OrderImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    pass
