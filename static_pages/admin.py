from django.contrib import admin
from static_pages.models import StaticPages


@admin.register(StaticPages)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'content', 'avatar')
    readonly_fields = ('avatar',)
