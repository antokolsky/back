import os
from dotenv import load_dotenv
from django.core.management import BaseCommand
from users.models import City, Country
import asyncio
from django.db.utils import OperationalError
import aiohttp
import copy

load_dotenv()


async def get_cities():

    connection = aiohttp.TCPConnector(limit_per_host=8)
    timeout = aiohttp.ClientTimeout(total=30)
    parameters: dict = {
        'apiKey': os.getenv('GEOHELPER_KEY'),
        'locale[lang]': os.getenv('GEOHELPER_LANG'),
        'locale[fallbackLang]': os.getenv('GEOHELPER_LANG'),
        'filter[countryIso]': 'AT',
        'pagination[limit]': 100
    }

    async with aiohttp.ClientSession(
            timeout=timeout,
            connector=connection
    ) as session:
        async with session.get(
                f'{os.getenv("GEOHELPER_URL")}/api/v1/cities',
                params=parameters
        ) as response:
            response = await response.json()
            pages = response.get('pagination').get('totalPageCount')
            print(pages)
            parameters_page = copy.deepcopy(parameters)
            print(parameters_page['filter[countryIso]'])
            country = await Country.objects.aget(
                iso=parameters_page['filter[countryIso]']
            )
            print(country)
            for page in range(1, pages + 1):
                parameters_page['pagination[page]'] = page
                async with session.get(
                        f'{os.getenv("GEOHELPER_URL")}/api/v1/cities',
                        params=parameters_page
                ) as response_page:
                    response_page = await response_page.json()
                    if response_page['success']:
                        await City.objects.abulk_create(
                            [
                                City(
                                    name_ru=city.get('name'),
                                    name_en=city['localizedNames']['en'],
                                    country=country
                                ) for city in response_page['result']
                            ]
                        )


class Command(BaseCommand):
    help: str = 'Import cities by countries from geohelper.info'

    def handle(self, *args, **options):
        try:
            if City.objects.count() > 0:
                print(
                    'В таблице уже есть данные. '
                    'Очистите таблицу вручную с очисткой primary key'
                )
            else:
                asyncio.get_event_loop().run_until_complete(get_cities())
        except OperationalError as e:
            print(f'{e}. Не проведены миграции.')
