from rest_framework import serializers  # Импорт классов сериализации из DRF.
from .models import Project, ProjectInterest  # Импорт моделей Project и ProjectInterest из текущей директории.


class ProjectSerializer(serializers.ModelSerializer):  # Определение сериализатора для модели Project.
    class Meta:
        model = Project  # Указание модели, которую сериализатор будет использовать.
        fields = '__all__'  # Указание, что необходимо сериализовать все поля модели.
        read_only_fields = (
        'owner', 'created_at', 'updated_at')  # Указание полей, которые будут доступны только для чтения.


class ProjectInterestSerializer(
    serializers.ModelSerializer):  # Определение сериализатора для модели интереса к проектам.
    class Meta:
        model = ProjectInterest  # Указание модели, которую сериализатор будет использовать.
        fields = '__all__'  # Сериализация всех полей модели.
        read_only_fields = ('user', 'created_at')  # Поля доступные только для чтения.
