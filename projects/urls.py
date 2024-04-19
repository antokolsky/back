from django.urls import path  # Импорт функции path для определения маршрутов URL.
from .views import ProjectListCreateView, ProjectDetailView, ProjectInterestCreateView  # Импорт представлений из
# текущего приложения.

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list'),  # URL для списка проектов и создания нового
    # проекта.
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),  # URL для просмотра, обновления и
    # удаления проекта по его ID (pk).
    path('<int:pk>/interest/', ProjectInterestCreateView.as_view(), name='project-interest'),  # URL для выражения
    # интереса к проекту по его ID (pk).
]
