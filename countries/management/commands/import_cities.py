import os
import copy
import asyncio

from dotenv import load_dotenv
import aiohttp
from tqdm.asyncio import trange
from django.core.management import BaseCommand
from django.db.utils import OperationalError

from countries.models import Country, City

load_dotenv()


async def async_generator(limit):
    for worker in range(1, limit + 1):
        yield worker


async def get_cities():
    connection = aiohttp.TCPConnector(limit=9)
    timeout = aiohttp.ClientTimeout(total=300)
    parameters = {
        'apiKey': os.getenv('GEOHELPER_KEY'),
        'locale[lang]': os.getenv('GEOHELPER_LANG'),
        'locale[fallbackLang]': os.getenv('GEOHELPER_LANG'),
        'pagination[limit]': 100,
    }
    async with aiohttp.ClientSession(
        timeout=timeout, connector=connection
    ) as session:
        async for country in Country.objects.values('iso', 'name_ru'):
            parameters['filter[countryIso]'] = country['iso']
            print(country['name_ru'])
            async with session.get(
                f'{os.getenv("GEOHELPER_URL")}/api/v1/cities',
                params=parameters,
            ) as response:
                response = await response.json()
                pages = response.get('pagination').get('totalPageCount')
                parameters_page = copy.deepcopy(parameters)
                country = await Country.objects.aget(
                    iso=parameters_page['filter[countryIso]']
                )
                all_cities = {}
                async for page in trange(1, pages + 1):
                    parameters_page['pagination[page]'] = page
                    async with session.get(
                        f'{os.getenv("GEOHELPER_URL")}/api/v1/cities',
                        params=parameters_page,
                    ) as response_page:
                        response_page_answer = await response_page.json()
                        if response_page_answer['success']:
                            for city in response_page_answer['result']:
                                if not city.get('name') in all_cities.keys():
                                    all_cities[city.get('name')] = city.get(
                                        'localizedNames'
                                    ).get('en')
                print(all_cities)
                await City.objects.abulk_create(
                    [
                        City(
                            name_ru=city_ru, name_en=city_en, country=country
                        )
                        for city_ru, city_en in all_cities.items()
                    ]
                )


class Command(BaseCommand):
    help = 'Import cities'

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
