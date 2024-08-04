from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters

from countries.models import Country
from countries.serializers import CountrySerializer


class CountryViewSet(ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_ru',)
    serializer_class = CountrySerializer
