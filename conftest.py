import pytest
from rest_framework.test import APIClient

from static_pages.models import StaticPages


@pytest.fixture
def create_user(django_user_model):
    django_user_model.objects.create_user(username='test')


@pytest.fixture
def api_client() -> APIClient:
    yield APIClient()


@pytest.fixture
def static_pages_list():
    all_pages = [
        StaticPages(
            title=f'Статическая страница №{page}',
            description=f'Описание страницы #{page}',
            content=f'Какой-то контент на странице №{page}',
        )
        for page in range(1, 6)
    ]

    return StaticPages.objects.bulk_create(all_pages)
