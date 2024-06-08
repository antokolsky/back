from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import CustomUserViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)

router_v1 = DefaultRouter()
router_v1.register("users", CustomUserViewSet, basename="users")

urlpatterns = [
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/", include("djoser.urls.authtoken")),
    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("", include(router_v1.urls)),
]
