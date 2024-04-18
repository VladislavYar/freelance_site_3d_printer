from django.urls import path

from api.v1.views import LocalityView


urlpatterns = [
    path("locations/", LocalityView.as_view(), name="locations"),
]
