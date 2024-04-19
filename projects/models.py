from django.db import models  # Импорт базовых классов моделей из Django.
from django.contrib.auth import get_user_model  # Импорт функции для получения текущей активной модели пользователя.
from django.core.validators import MinValueValidator, MaxValueValidator  # Импорт валидаторов для проверки значений.
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

User = get_user_model()  # Получение модели пользователя, используемой в проекте.


class Project(models.Model):  # Определение новой модели Project, наследуемой от Model.
    name = models.CharField(max_length=255,
                            unique=True)  # Поле для названия проекта, уникальное, максимум 255 символов.
    description = models.CharField(max_length=500)  # Поле описания проекта, ограничено 500 символами.
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  # Поле стоимости
    # с валидацией, что она не может быть отрицательной.
    has_3d_model = models.BooleanField(default=False)  # Булево поле, указывающее наличие 3D модели.
    owner = models.ForeignKey(User, related_name='owned_projects',
                              on_delete=models.CASCADE)  # Внешний ключ к модели пользователя. Указывает на владельца
    # проекта.
    created_at = models.DateTimeField(
        auto_now_add=True)  # Поле даты создания проекта, устанавливается автоматически при создании.
    updated_at = models.DateTimeField(
        auto_now=True)  # Поле даты последнего обновления проекта, устанавливается автоматически при каждом сохранении.
    photos = ProcessedImageField(upload_to='project_photos',
                                 processors=[ResizeToFill(100, 50)],
                                 format='JPEG',
                                 options={'quality': 60})

    def __str__(self):
        return self.name  # Метод для отображения объекта в виде строки, возвращает имя проекта.


class ProjectInterest(models.Model):  # Определение модели интереса к проектам.
    project = models.ForeignKey(Project, related_name='interested_users',
                                on_delete=models.CASCADE)  # Внешний ключ к модели Project.
    user = models.ForeignKey(User, related_name='interested_projects',
                             on_delete=models.CASCADE)  # Внешний ключ к модели пользователя, указывает на
    # пользователя, проявившего интерес.
    created_at = models.DateTimeField(
        auto_now_add=True)  # Поле даты проявления интереса, устанавливается автоматически при создании.

    class Meta:
        unique_together = ('project',
                           'user')  # Уникальный составной ключ, не позволяющий пользователю проявить интерес к
        # проекту более одного раза.

    def __str__(self):
        return f"{self.user.username} - {self.project.name}"  # Строковое представление объекта, включает имя
        # пользователя и название проекта.
