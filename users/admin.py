from django.contrib import admin
from django.utils.safestring import mark_safe

from users.models import User


def lists(model, model_field=None):
    fields = [field.name for field in model._meta.fields]
    if model_field:
        fields.append(model_field)
    return fields


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'is_seller',
        'personal_account_filled',
    )
    list_display_links = ('id', 'username', 'email')
    search_fields = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        (
            'Роли',
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                    'is_active',
                    'is_seller',
                    'personal_account_filled',
                )
            },
        ),
        (
            'Личная информация',
            {
                'fields': (
                    'avatar_preview',
                    'avatar',
                    'first_name_ru',
                    'first_name_eng',
                    'last_name_ru',
                    'last_name_en',
                    'about_ru',
                    'about_en',
                    'country',
                    'address',
                    'communication_method',
                )
            },
        ),
        ('Стили и материалы', {'fields': ('style', 'materials')}),
    )
    readonly_fields = ('avatar_preview', 'created_at')

    def avatar_preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width="100px">')
