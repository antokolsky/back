import json

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_main_page(api_client, static_pages_list, create_user):
    response = api_client.get('/api/russian/index/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data != [], 'Вернулись пусты данные'
    response = json.loads(response.content)
    assert response[0]['static_posts'] == [], response[0]['static_posts']
