from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.db import models
from PIL import Image

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


class LandingProject(models.Model):
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
    )
    cost = models.PositiveIntegerField('Стоимость')
    rating = models.IntegerField('Рейтинг', default=RATING_DEFAULT)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('-rating', 'cost')

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        LandingProject,
        on_delete=models.CASCADE,
        related_name='project_images',
    )
    image = models.ImageField(
        'Изображение', upload_to='landing/project_images/'
    )
    preview_image = models.ImageField(
        'Превью изображения',
        blank=True,
        null=True,
        upload_to=('landing/project_images/previews/'),
    )

    class Meta:
        verbose_name = 'Изображение проекта'
        verbose_name_plural = 'Изображения проекта'
        ordering = ('project', 'image')

    def __str__(self):
        return self.project.title

    def save(self, *args, **kwargs):
        super(ProjectImage, self).save(*args, **kwargs)
        img = Image.open(self.preview_image.path)
        max_size = (78, 86)
        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(size=max_size)
            img = img.convert('RGB')
            img.save(self.preview_image.path)


class VolumetricModel(models.Model):
    low = models.FileField(
        'Файл низкого разрешения', upload_to='landing/volumetric_models_low'
    )
    high = models.FileField(
        'Файл высокого разрешения', upload_to='landing/volumetric_models_high'
    )

    class Meta:
        verbose_name = '3D Модель'
        verbose_name_plural = '3D Модели'

    def __str__(self):
        return self.high.name


class ActivityType(models.Model):
    name = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = 'Тип деятельности'
        verbose_name_plural = 'Типы деятельности'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Respondent(models.Model):
    email = models.EmailField('E-mail', max_length=254, unique=True)
    country = models.CharField('Страна', max_length=50)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    organization = models.CharField('Организация', max_length=50)
    organization_website = models.URLField('Сайт', blank=True, null=True)

    class Meta:
        verbose_name = 'Респондент'
        verbose_name_plural = 'Респонденты'
        ordering = ('organization',)

    def __str__(self):
        return self.organization
