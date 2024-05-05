import os
from http import HTTPStatus

import requests
from django.core.management.base import BaseCommand
from dotenv import load_dotenv

from users.models import Country

load_dotenv()


class Command(BaseCommand):
    help: str = 'Import countries from geohelper.info'
    parameters: dict = {
        'apiKey': os.getenv('GEOHELPER_KEY'),
        'locale[lang]': os.getenv('GEOHELPER_LANG'),
        'locale[fallbackLang]': os.getenv('GEOHELPER_LANG')
    }
    clear_message_text: str = 'Очищаем таблицу'
    adding_message_text: str = 'Добавляем страны'

    def handle(self, *args, **options):
        with requests.session() as session:
            with session.get(
                f'{os.getenv("GEOHELPER_URL")}/api/v1/countries',
                params=self.parameters
            ) as response:
                if response.status_code == HTTPStatus.OK:
                    response = response.json()
                    if response['success']:
                        if Country.objects.count() > 0:
                            print(self.clear_message_text)
                            count = Country.objects.count()
                            Country.objects.all().delete()
                            print(f'{count} записей удалены')
                        print(self.adding_message_text)
                        Country.objects.bulk_create(
                            [
                                Country(
                                    name_ru=country['name'],
                                    name_en=country['localizedNames']['en']
                                )
                                for country in response['result']
                            ]
                        )
                        print(f'{Country.objects.count()} записей добавлено')
                else:
                    print(response.status_code)
        