from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView, StyleListView, MaterialListView

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list'),
    path('<uuid:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('styles/', StyleListView.as_view(), name='style-list'),
    path('materials/', MaterialListView.as_view(), name='material-list'),
]
