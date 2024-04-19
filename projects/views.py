from rest_framework import generics, permissions  # Импорт базовых классов представлений и классов разрешений из DRF.
from rest_framework.exceptions import PermissionDenied

from .models import Project, ProjectInterest  # Импорт моделей из текущего приложения.
from .serializers import ProjectSerializer, ProjectInterestSerializer  # Импорт сериализаторов для этих моделей.
from django.shortcuts import \
    get_object_or_404  # Импорт функции для получения объекта или возвращения ошибки 404, если объект не найден.
from rest_framework.response import Response  # Импорт класса Response для возвращения ответов из представлений.


# Для создания и списка проектов
class ProjectListCreateView(
    generics.ListCreateAPIView):  # Наследование от класса представления для списка и создания объектов.
    queryset = Project.objects.all()  # Указание набора объектов, который будет использоваться для представления.
    serializer_class = ProjectSerializer  # Указание сериализатора для обработки данных модели.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Установка разрешений для представления.

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user)  # Метод для сохранения нового проекта с присвоением владельца текущему
        # пользователю.


# Для деталей, обновления и удаления проектов
class ProjectDetailView(
    generics.RetrieveUpdateDestroyAPIView):  # Наследование от класса представления для получения, обновления и
    # удаления объектов.
    queryset = Project.objects.all()  # Указание набора объектов для представления.
    serializer_class = ProjectSerializer  # Сериализатор для обработки данных модели.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Разрешения для представления.

    def perform_update(self, serializer):
        project = self.get_object()  # Получение текущего объекта проекта.
        if self.request.user == project.owner:
            serializer.save()  # Сохранение изменений, если текущий пользователь является владельцем.
        else:
            raise PermissionDenied(
                "You do not have permission to edit this project.")  # Выброс исключения, если пользователь не
            # является владельцем.


# Для выражения интереса к проекту
class ProjectInterestCreateView(generics.CreateAPIView):  # Наследование от класса представления для создания объекта.
    serializer_class = ProjectInterestSerializer  # Сериализатор для обработки данных модели интереса к проекту.
    permission_classes = [permissions.IsAuthenticated]  # Установка разрешений для представления.

    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))  # Получение проекта или возврат 404 ошибки.
        if self.request.user == project.owner:
            raise PermissionDenied(
                "You cannot express interest in your own project.")  # Выброс исключения, если пользователь пытается
            # выразить интерес к своему проекту.
        serializer.save(user=self.request.user,
                        project=project)  # Сохранение нового объекта интереса с текущим пользователем и проектом.
