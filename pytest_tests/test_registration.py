import pytest

from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()


@pytest.mark.django_db
@pytest.mark.parametrize(
    'url, is_seller',
    (('/api/russian/users/', True), ('/api/english/users/', False)),
)
def test_registration_russian_user(api_client, url, is_seller):
    payload = {
        'username': 'test_user',
        'password': 'test_password',
        'email': 'test_user@test.com',
    }
    response_registration = api_client.post(url, data=payload, format='json')
    assert (
        response_registration.status_code == status.HTTP_201_CREATED
    ), f'Ответ не равен статусу {status.HTTP_201_CREATED}'
    assert (
        User.objects.filter(username=payload['username']).exists() is True
    ), 'Только что созданный пользователь не найден в БД'
    assert (
        User.objects.get(email=payload['email']).is_seller is is_seller
    ), f"Только что созданный пользователь не является продавцом"
