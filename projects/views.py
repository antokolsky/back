from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Project, Style, Material
from .serializers import ProjectSerializer, StyleSerializer, MaterialSerializer
from .permissions import IsAuthorOrAdmin


class ProjectListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания нового проекта и получения списка всех проектов.

    - Доступ к просмотру имеют все пользователи.
    - Создание проекта доступно только аутентифицированным пользователям,
      которые заполнили информацию о себе в личном кабинете.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        """
        Создает новый проект с текущим пользователем в качестве автора.

        - Проверяет, заполнен ли профиль пользователя.
        - Если профиль не заполнен, выдает ошибку PermissionDenied.
        """
        if not self.request.user.profile.is_filled:
            raise PermissionDenied("Вам необходимо заполнить свой профиль, чтобы создать проект.")
        serializer.save(author=self.request.user)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для получения, обновления и удаления проекта.

    - Доступ к просмотру имеют все пользователи.
    - Обновление и удаление проекта доступно только его автору или модератору.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthorOrAdmin]

    def perform_update(self, serializer):
        """
        Обновляет проект с данными из сериализатора.
        """
        serializer.save()


class StyleListView(generics.ListAPIView):
    """
    Представление для получения списка всех стилей.

    - Доступ к просмотру имеют все пользователи.
    """
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    permission_classes = [permissions.AllowAny]


class MaterialListView(generics.ListAPIView):
    """
    Представление для получения списка всех материалов.

    - Доступ к просмотру имеют все пользователи.
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.AllowAny]
