from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator
)

AUTHOR_NAME_VERBOSE = 'Имя автора'
AUTHOR_NAME_LENGTH_VALIDATION_MAX = 200
AUTHOR_NAME_LENGTH_VALIDATION_MIN = 1
AUTHOR_NAME_LENGTH_VALIDATION_MIN_MESSAGE = (
    'Имя автора должно быть длинее {} символа'
)
AUTHOR_NAME_LENGTH_VALIDATION_MAX_MESSAGE = (
    'Имя автора должно быть короче {} символов'
)

TITLE_MIN_LENGTH = 1
TITLE_MAX_LENGTH = 100
TITLE_MIN_LENGTH_ERROR_MESSAGE = (
    'Название работы должно быть длинее {} символа'
)
TITLE_MAX_LENGTH_ERROR_MESSAGE = (
    'Название работы должно быть короче {} символов'
)
TITLE_VERBOSE = 'Название работы'

DIMENSION_HEIGHT_NAME = 'Высота'
DIMENSION_WIDTH_NAME = 'Ширина'
DIMENSION_DEPTH_NAME = 'Глубина'
DIMENSION_MIN_VALUE = 1
DIMENSION_MAX_VALUE = 65535
DIMENSION_VALIDATOR_MESSAGE = '{} должна быть больше или равна {} см.'

COST_MAX = 100000
RATING_DEFAULT = 0

MATERIAL_VERBOSE = 'Материал'


class Material(models.Model):
    name_ru = models.CharField('Название на русском', max_length=100)
    name_eng = models.CharField('Название на английском', max_length=100)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ('name_ru',)
        unique_together = ('name_ru', 'name_eng')

    def __str__(self):
        return f'Создан материал: {self.name_ru} - {self.name_eng}'


class Project(models.Model):
    author_name = models.CharField(
        AUTHOR_NAME_VERBOSE,
        max_length=AUTHOR_NAME_LENGTH_VALIDATION_MAX,
        validators=[
            MinLengthValidator(
                AUTHOR_NAME_LENGTH_VALIDATION_MIN,
                message=AUTHOR_NAME_LENGTH_VALIDATION_MIN_MESSAGE.format(
                    AUTHOR_NAME_LENGTH_VALIDATION_MIN
                ),
            ),
            MaxLengthValidator(
                AUTHOR_NAME_LENGTH_VALIDATION_MAX,
                message=AUTHOR_NAME_LENGTH_VALIDATION_MAX_MESSAGE.format(
                    AUTHOR_NAME_LENGTH_VALIDATION_MAX
                ),
            ),
        ],
    )
    title = models.CharField(
        TITLE_VERBOSE,
        validators=[
            MinLengthValidator(
                TITLE_MIN_LENGTH,
                message=TITLE_MIN_LENGTH_ERROR_MESSAGE.format(
                    TITLE_MIN_LENGTH
                ),
            ),
            MaxLengthValidator(
                TITLE_MAX_LENGTH,
                message=TITLE_MAX_LENGTH_ERROR_MESSAGE.format(
                    TITLE_MAX_LENGTH
                ),
            ),
        ],
        max_length=TITLE_MAX_LENGTH,
    )
    dimension_height = models.PositiveSmallIntegerField(
        DIMENSION_HEIGHT_NAME,
        validators=[
            MinValueValidator(
                DIMENSION_MIN_VALUE,
                message=DIMENSION_VALIDATOR_MESSAGE.format(
                    DIMENSION_HEIGHT_NAME, DIMENSION_MIN_VALUE
                ),
            )
        ],
        max_length=DIMENSION_MAX_VALUE,
    )
    dimension_width = models.PositiveSmallIntegerField(
        DIMENSION_WIDTH_NAME,
        validators=[
            MinValueValidator(
                DIMENSION_MIN_VALUE,
                message=DIMENSION_VALIDATOR_MESSAGE.format(
                    DIMENSION_WIDTH_NAME, DIMENSION_MIN_VALUE
                ),
            )
        ],
        max_length=DIMENSION_MAX_VALUE,
    )
    dimension_depth = models.PositiveSmallIntegerField(
        DIMENSION_DEPTH_NAME,
        validators=[
            MinValueValidator(
                DIMENSION_MIN_VALUE,
                message=DIMENSION_VALIDATOR_MESSAGE.format(
                    DIMENSION_DEPTH_NAME, DIMENSION_MIN_VALUE
                ),
            )
        ],
        max_length=DIMENSION_MAX_VALUE,
    )
    cost = models.PositiveIntegerField('Стоимость', max_length=COST_MAX)
    rating = models.IntegerField('Рейтинг', default=RATING_DEFAULT)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('-rating', 'cost')

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_images'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='landing/project_images'
    )
    preview_image = models.ImageField(
        'Превью изображения',
        blank=True,
        null=True,
        height_field='86'
    )

    class Meta:
        verbose_name = 'Изображение проекта'
        verbose_name_plural = 'Изображения проекта'
        ordering = ('project', 'image')

# TODO Дописать модель для Респондента
# TODO Дописать модель для формы заказа
# TODO Дописать модель для Рода деятельности респондента
