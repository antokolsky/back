import pytest
from rest_framework import status


@pytest.mark.django_db
def test_registration_russian_user(api_client):
    payload = {
        'username': 'test_user',
        'password':  'test_password',
        'email':  'test_user@test.com',
    }
    response_registration = api_client.post(
        '/api/russian/users/', data=payload, format='json'
    )
    assert response_registration.status_code == status.HTTP_201_CREATED
