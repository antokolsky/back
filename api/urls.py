from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import (  # CountryViewSet,; RandomUsersOnMainPageViewSet,; IndexPageViewSet,
    CustomUserEnglishViewSet,
    CustomUserRussianViewSet,
    ProjectViewSet,
    RandomProjectsOnMainPageViewSet,
    StaticPagesViewSet,
)
from countries.views import CountryViewSet

router_eng = DefaultRouter()
router_eng.register("users", CustomUserEnglishViewSet, basename="eng_users")

router_ru = DefaultRouter()
router_ru.register("users", CustomUserRussianViewSet, basename="users")
# router_ru.register("countries", CountryViewSet, basename="countries")
router_ru.register(
    'static_pages', StaticPagesViewSet, basename="static_pages"
)
# router_ru.register('index', IndexPageViewSet, basename="main_page")
router_ru.register('projects', ProjectViewSet, basename="projects")
router_ru.register(
    'random_projects_on_main_page',
    RandomProjectsOnMainPageViewSet,
    basename="random_projects_on_main_page",
)
# router_ru.register(
#     'random_authors_on_main_page',
#     RandomUsersOnMainPageViewSet,
#     basename='random_authors_on_main_page',
# )
router_countries = DefaultRouter()
router_countries.register('', CountryViewSet, basename='country')
urlpatterns = [
    path(
        "auth/get_token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("english/", include(router_eng.urls)),
    path("russian/", include(router_ru.urls)),
    path('countries/', include(router_countries.urls)),
]
