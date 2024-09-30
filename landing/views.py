from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from landing.models import ActivityType, Respondent, LandingProject
from landing.serializers import (
    ActivityTypeSerializer,
    RespondentReadSerializer,
    RespondentWriteSerializer,
    LandingProjectSerializer,
)


class ActivityTypeViewSet(ReadOnlyModelViewSet):
    '''Получение списка родов деятельности респондента.'''

    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer


class RespondentViewSet(ModelViewSet):
    '''Получение списка респондентов.'''

    queryset = Respondent.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RespondentReadSerializer
        return RespondentWriteSerializer


class LandingProjectViewSet(ReadOnlyModelViewSet):
    '''Получение списка проектов.'''

    queryset = LandingProject.objects.all()
    serializer_class = LandingProjectSerializer
