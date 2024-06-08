from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import CustomUserViewSet, CountryViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)

router_v1 = DefaultRouter()
router_v1.register("users", CustomUserViewSet, basename="users")
router_v1.register("countries", CountryViewSet, basename="countries")

urlpatterns = [
    path(
        "auth/get_token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(router_v1.urls)),
]
