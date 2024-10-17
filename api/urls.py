from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import (
    CountryViewSet,
    CustomUserEnglishViewSet,
    CustomUserRussianViewSet,
    IndexPageViewSet,
    ProjectViewSet,
    RandomProjectsOnMainPageViewSet,
    RandomUsersOnMainPageViewSet,
    StaticPagesViewSet,
)
from landing.views import (
    ActivityTypeViewSet,
    RespondentViewSet,
    LandingProjectViewSet,
    SculptureOrderViewSet,
)

router_eng = DefaultRouter()
router_eng.register("users", CustomUserEnglishViewSet, basename="eng_users")

router_ru = DefaultRouter()
router_ru.register("users", CustomUserRussianViewSet, basename="users")
router_ru.register("countries", CountryViewSet, basename="countries")
router_ru.register(
    'static_pages', StaticPagesViewSet, basename="static_pages"
)
router_ru.register('index', IndexPageViewSet, basename="main_page")
router_ru.register('projects', ProjectViewSet, basename="projects")
router_ru.register(
    'random_projects_on_main_page',
    RandomProjectsOnMainPageViewSet,
    basename="random_projects_on_main_page",
)
router_ru.register(
    'random_authors_on_main_page',
    RandomUsersOnMainPageViewSet,
    basename='random_authors_on_main_page',
)

router_landing = DefaultRouter()
router_landing.register(
    'activity_types', ActivityTypeViewSet, basename='activity_types'
)
router_landing.register(
    'respondents', RespondentViewSet, basename='respondents'
)
router_landing.register(
    'projects', LandingProjectViewSet, basename='_projects'
)
router_landing.register(
    'sculpture_order', SculptureOrderViewSet, basename='sculpture_order'
)

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
    path('landing/', include(router_landing.urls)),
]
