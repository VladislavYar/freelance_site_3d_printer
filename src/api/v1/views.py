from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from api.v1.serializers import LocalitySerializer
from order.models import Locality


class LocalityView(ListAPIView):
    """Отдаёт список населённых пунктов."""
    queryset = Locality.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = LocalitySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'region',
        'city_type',
        'city',
        )
