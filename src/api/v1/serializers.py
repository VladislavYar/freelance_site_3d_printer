from rest_framework.serializers import ModelSerializer

from order.models import Locality


class LocalitySerializer(ModelSerializer):
    """Сериализатор населённых пунктов."""
    class Meta:
        model = Locality
        fields = (
            'id',
            'region',
            'city_type',
            'city',
            )
