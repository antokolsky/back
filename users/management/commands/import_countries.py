import asyncio
import os
from http import HTTPStatus

import aiohttp
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from dotenv import load_dotenv
from tqdm import tqdm

from users.models import Country

load_dotenv()


async def get_countries(params):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'{os.getenv("GEOHELPER_URL")}/api/v1/countries',
                params=params
        ) as response:
            if response.status == HTTPStatus.OK:
                response = await response.json()
                if response['result']:
                    if response['success']:
                        await Country.objects.abulk_create(
                            [
                                Country(
                                    name_ru=country['name'],
                                    name_en=country['localizedNames']['en'],
                                    iso=country.get('iso')
                                ) for country in tqdm(response['result'])
                            ]
                        )
                    else:
                        print(
                            'Статус ответа сервера отрицательный. '
                            'Проверьте ключ'
                        )
                else:
                    print('В ответе не найдены данные о странах')


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
        try:
            if Country.objects.last():
                print(
                    'В таблице уже есть данные. '
                    'Очистите таблицу вручную с очисткой primary key'
                )
            else:
                asyncio.get_event_loop().run_until_complete(
                    get_countries(self.parameters)
                )
        except OperationalError as e:
            print(f'{e}. Не проведены миграции!')
