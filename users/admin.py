from django.contrib import admin
from users.models import User, Country, UserInfo, Style, Material
from django.utils.safestring import mark_safe


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name_ru',
        'first_name_eng',
        'last_name_ru',
        'last_name_en',
        'avatar_preview',
    )
    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width="100px">')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en')


# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth import get_user_model
#
# # Получаем модель пользователя, которую мы настроили в файле settings.py
# User = get_user_model()
#
#
# # Определяем новый класс UserAdmin для кастомизации отображения
# class UserAdmin(BaseUserAdmin):
#     # Список полей, которые будут отображаться в списке пользователей
#     list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
#
#     # Список полей, которые будут использоваться для фильтрации пользователей
#     list_filter = ('is_staff', 'is_superuser', 'is_active')
#
#     # Список полей, которые будут использоваться для поиска
#     search_fields = ('username', 'email')
#
#     # Порядок следования полей при редактировании/добавлении пользователя
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                     'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2'),
#         }),
#     )
#
#     # Настройки для сортировки пользователей
#     ordering = ('username',)
#
#
# # Регистрируем модель User с кастомным UserAdmin
# admin.site.register(User, UserAdmin)
