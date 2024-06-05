from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import CountryViewSet, CustomUserViewSet

router_v1 = DefaultRouter()
router_v1.register("users", CustomUserViewSet, basename="users")
router_v1.register("countries", CountryViewSet, basename="countries")

urlpatterns = [
    path(
        "auth/get_tokens",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("auth/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("", include(router_v1.urls)),
]
