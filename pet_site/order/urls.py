from django.urls import path
from order.views import index


app_name = 'order'


urlpatterns = [
    path('', index, name='index'),
]
