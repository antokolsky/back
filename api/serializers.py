from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from users.models import Country, UserInfo

User = get_user_model()


class CustomUserEnglishSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("is_seller",)


class CountrySerializer(ModelSerializer):
    """Сериализатор модели Стран."""

    class Meta:
        model = Country
        fields = "__all__"


class UserInfoReadSerializer(ModelSerializer):
    """Сериализатор модели Информации о пользователе."""

    class Meta:
        model = UserInfo
        fields = "__all__"
