from django.urls import path
from order.views import index, order, order_delete


app_name = 'order'


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', order, name='order'),
    path('<int:pk>/delete', order_delete, name='order-delete'),
]
