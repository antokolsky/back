from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from landing.models import (
    ActivityType,
    LandingProject,
    Respondent,
    SculptureOrder
)
from landing.serializers import (
    ActivityTypeSerializer,
    LandingProjectSerializer,
    RespondentReadSerializer,
    RespondentWriteSerializer,
    SculptureOrderSerializer
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

    @action(methods=('POST',), detail=True)
    def vote(self, request, pk):
        """
        Метод для голосования.
        В зависимости от параметра action увеличивает или уменьшает рейтинг
        проекта.
        Если action=unvote, то уменьшает рейтинг проекта.
        """
        project = get_object_or_404(LandingProject, id=pk)
        if self.request.GET.get('action', False) == 'unvote':
            project.rating -= 1
        else:
            project.rating += 1
        project.save()
        return Response({'status': 'Updated'}, status=status.HTTP_200_OK)


class SculptureOrderViewSet(ModelViewSet):
    """
    Метод для создания заказов скульптур.
    """
    queryset = SculptureOrder.objects.all()
    http_method_names = ('post', 'get')
    serializer_class = SculptureOrderSerializer
