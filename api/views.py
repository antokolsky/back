from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from api.serializers import (
    CountrySerializer,
    UserInfoReadSerializer,
    CustomUserEnglishSerializer,
)
from users.models import Country, UserInfo

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()


class CustomUserEnglishViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserEnglishSerializer

    def perform_create(self, serializer):
        serializer.save(is_seller=True)


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return UserInfoReadSerializer
        return CountrySerializer


class CountryViewSet(ReadOnlyModelViewSet):
    """ViewSet for the Country model."""

    queryset = Country.objects.all()
    pagination_class = None
    serializer_class = CountrySerializer
