from django.contrib import admin

from landing.models import (
    ActivityType,
    Respondent,
    VolumetricModel,
    LandingProject,
    ProjectImage,
)


class ProjectGalleryInline(admin.TabularInline):
    fk_name = 'project'
    model = ProjectImage


@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Respondent)
class RespondentAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'country',
        'organization',
        'organization_website',
    )
    list_filter = ('country',)


@admin.register(VolumetricModel)
class VolumetricModelAdmin(admin.ModelAdmin):
    list_display = ('low', 'high')


@admin.register(LandingProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'author_name',
        'title',
        'dimension_height',
        'dimension_width',
        'dimension_depth',
        'cost',
        'rating',
    )
    inlines = [ProjectGalleryInline]
