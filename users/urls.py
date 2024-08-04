from django.urls import path
from .views import CreateUserView, CustomAuthToken


urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
