from rest_framework.serializers import ModelSerializer

from users.models import Country


class CountrySerializer(ModelSerializer):
    """Сериализатор модели Стран."""
    class Meta:
        model = Country
        fields = '__all__'
