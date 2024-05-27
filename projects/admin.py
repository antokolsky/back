from django.contrib import admin
from .models import Project, Style, Material


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name_ru', 'name_en', 'avatar', 'description_ru', 'description_en',
        'other_photos', 'style', 'material', 'prepayment', 'cost_of_project', 'total_cost',
        'address', 'created_at', 'updated_at', 'is_moderated', 'author_id',
    ]
    search_fields = ['name_ru', 'style', 'material', 'address', 'created_at', 'updated_at', 'author_id']
    list_filter = [
        'is_moderated', 'style', 'material', 'created_at', 'updated_at', 'author_id'
        'style', 'material', 'prepayment', 'cost_of_project', 'total_cost',
    ]


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'name_en']
    search_fields = ['name_ru', 'name_en']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'name_en']
    search_fields = ['name_ru', 'name_en']