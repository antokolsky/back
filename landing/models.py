from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator,
)

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
DIMENSION_HEIGHT_NAME = 'Высота'
DIMENSION_WIDTH_NAME = 'Ширина'
DIMENSION_DEPTH_NAME = 'Глубина'
DIMENSION_MIN_VALUE = 1
DIMENSION_MAX_VALUE = 65535
DIMENSION_VALIDATOR_MESSAGE = '{} должна быть больше или равна {} см.'


class Project(models.Model):
    author_name = models.CharField(
        'Имя автора',
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
        'Название работы',
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
    cost = models.PositiveIntegerField('Стоимость', max_length=100000)
    rating = models.IntegerField('Рейтинг', default=0)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('-rating', 'cost')

    def __str__(self):
        return self.title
