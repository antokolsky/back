from django.contrib import admin
from static_pages.models import StaticPages
from django.utils.safestring import mark_safe


@admin.register(StaticPages)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'content', 'avatar_preview'
    )
    readonly_fields = ('avatar_preview',)

    @staticmethod
    def avatar_preview(obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width="50px"')
