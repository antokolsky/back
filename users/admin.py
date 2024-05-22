from django.contrib import admin
from users.models import User, Country


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')


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
