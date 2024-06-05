import re

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import CountrySerializer
from users.models import Country, UserInfo

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()

    @action(
        detail=True,
        methods=("POST", "GET"),
        permission_classes=(IsAuthenticated,),
    )
    def user_info(self, request, id: int):
        user: int = request.user.id
        if int(id) != int(user):
            return Response(
                {"errors": f"Not allowed for this user {user}, id={id}"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return Response("None", status=status.HTTP_200_OK)
        user_information = get_object_or_404(UserInfo, user=id)


class CountryViewSet(ReadOnlyModelViewSet):
    """ViewSet for the Country model."""

    queryset = Country.objects.all()
    pagination_class = None
    serializer_class = CountrySerializer
