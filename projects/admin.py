from django.contrib import admin
from .models import Project, ProjectInterest


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'cost', 'has_3d_model', 'created_at', 'updated_at']
    search_fields = ['name', 'description']


@admin.register(ProjectInterest)
class ProjectInterestAdmin(admin.ModelAdmin):
    list_display = ['project', 'user', 'created_at']
    search_fields = ['project__name', 'user__username']
