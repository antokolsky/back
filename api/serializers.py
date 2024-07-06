from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from projects.models import Project
from static_pages.models import StaticPages
from users.models import Country, UserInfo

User = get_user_model()


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("is_seller",)


class UserListSerializer(ModelSerializer):
    """Сериализатор модели для списка пользователей на главной странице."""

    class Meta:
        model = UserInfo
        fields = ('avatar', 'first_name_ru', 'last_name_ru')


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


class StaticPageSerializer(ModelSerializer):
    """Сериализатор модели Статических страниц."""

    class Meta:
        model = StaticPages
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    """Сериализатор модели Статических страниц."""

    class Meta:
        model = Project
        fields = '__all__'


class ProjectOnMainPageSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'cost', 'photos')
