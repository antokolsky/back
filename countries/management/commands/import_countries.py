import asyncio
import os
from http import HTTPStatus

import aiohttp
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from dotenv import load_dotenv
from tqdm import tqdm

from countries.models import Country

WRONG_RESPONSE_STATUS_CODE: str = 'Статус ответа сервера {}. Проверьте ключ'
WRONG_ANSWER_WITHOUT_KEY_RESULT: str = 'В ответе не найден ключ "result"'
WRONG_ANSWER_WITHOUT_KEY_SUCESS: str = 'В ответе не найден ключ "success"'
SUCCES_IMPORT: str = 'Успешно импортировано {} записей.'
CLEAR_MESSAGE_TEXT: str = (
    'В таблице уже есть данные. '
    'Очистите таблицу вручную с очисткой primary key'
)
ADDING_MESSAGE_TEXT: str = 'Добавляем страны'

load_dotenv()


async def get_countries(parameters):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{os.getenv("GEOHELPER_URL")}/api/v1/countries',
            params=parameters,
        ) as response:
            if response.status == HTTPStatus.OK:
                response_json = await response.json()
                if not response_json.get('result'):
                    print(WRONG_ANSWER_WITHOUT_KEY_RESULT)
                if not response_json.get('success'):
                    print(WRONG_ANSWER_WITHOUT_KEY_SUCESS)
                await Country.objects.abulk_create(
                    [
                        Country(
                            name_ru=country.get('name'),
                            name_en=country.get('localizedNames').get('en'),
                            iso=country.get('iso'),
                        )
                        for country in tqdm(response_json.get('result'))
                    ]
                )
                count = await Country.objects.all().acount()
                print(SUCCES_IMPORT.format(count))
            else:
                print(WRONG_RESPONSE_STATUS_CODE.format(response.status))


class Command(BaseCommand):
    help: str = 'Импортирует страны'
    parameters: dict = {
        'apiKey': os.getenv('GEOHELPER_KEY'),
        'locale[lang]': os.getenv('GEOHELPER_LANG'),
        'locale[fallbackLang]': os.getenv('GEOHELPER_LANG'),
    }

    def handle(self, *args, **options):
        try:
            empty_keys = []
            for parameter_name, parameter_value in self.parameters.items():
                if not parameter_value:
                    empty_keys.append(parameter_name)
            if len(empty_keys) == 1:
                raise ValueError(
                    'Ключ: {} не найден в виртуальном окружении'.format(
                        ''.join(empty_keys)
                    )
                )
            if len(empty_keys) > 1:
                raise ValueError(
                    'Ключи: {} не найдены в виртуальном окружении'.format(
                        ', '.join(empty_keys)
                    )
                )
            if Country.objects.last():
                print(CLEAR_MESSAGE_TEXT)
            else:
                asyncio.get_event_loop().run_until_complete(
                    get_countries(self.parameters)
                )
        except OperationalError as e:
            print(f'{e}. Не проведены миграции')
        except ValueError as e:
            print(e)
