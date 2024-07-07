from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    SAFE_METHODS,
)
from rest_framework.response import Response
from rest_framework.viewsets import (
    ModelViewSet,
    ReadOnlyModelViewSet,
    mixins,
    GenericViewSet,
)

from api.serializers import (
    CountrySerializer,
    UserInfoReadSerializer,
    CustomUserSerializer,
    StaticPageSerializer,
    ProjectSerializer,
    ProjectOnMainPageSerializer,
    UserListSerializer,
    MainPageRuSerializer,
)
from projects.models import Project
from static_pages.models import StaticPages
from users.models import Country, UserInfo

User = get_user_model()


class CustomUserRussianViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        serializer.save(is_seller=False)

    @action(
        detail=True, methods=('get',), permission_classes=[IsAuthenticated]
    )
    def on_main_page(self, request, id):
        """Returning the list of projects of the logged user for itself."""
        if request.user.id == int(id):
            if not Project.objects.filter(owner=request.user).count() > 0:
                return Response(status=status.HTTP_204_NO_CONTENT)
            queryset = Project.objects.filter(owner=request.user).order_by(
                '-id'
            )[:6]
            serializer = ProjectOnMainPageSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'error': 'You are not allowed to access this resource'},
            status=status.HTTP_403_FORBIDDEN,
        )


class RandomUsersOnMainPageViewSet(ReadOnlyModelViewSet):
    queryset = UserInfo.objects.filter(user__is_seller=True).order_by('?')[:3]
    serializer_class = UserListSerializer


class CustomUserEnglishViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

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


class StaticPagesViewSet(ReadOnlyModelViewSet):
    """ViewSet for the StaticPages model."""

    queryset = StaticPages.objects.all()
    pagination_class = None
    serializer_class = StaticPageSerializer


class ProjectViewSet(ReadOnlyModelViewSet):
    """ViewSet Для вывода на главную страницу"""

    queryset = Project.objects.all()
    pagination_class = None
    serializer_class = ProjectSerializer


class RandomProjectsOnMainPageViewSet(ReadOnlyModelViewSet):
    """Returning random projects on main page"""

    queryset = Project.objects.order_by('?')[:6]
    serializer_class = ProjectOnMainPageSerializer


class IndexPageViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = MainPageRuSerializer
