from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, SerializerMethodField

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


class MainPageRuSerializer(ModelSerializer):
    static_posts = SerializerMethodField()
    own_works = SerializerMethodField()

    def get_static_posts(self, obj) -> list[dict]:
        results = StaticPages.objects.all().order_by('id')
        return StaticPageSerializer(results, many=True).data

    def get_own_works(self, obj) -> list[dict]:
        user = self.context['request'].user
        if user.is_anonymous or not user.is_seller:
            return []
        else:
            if Project.objects.filter(owner=user).count == 0:
                return []
            else:
                results = Project.objects.filter(owner=user).order_by('-id')
                return ProjectOnMainPageSerializer(results, many=True).data

    class Meta:
        model = User
        fields = ('static_posts', 'own_works')
