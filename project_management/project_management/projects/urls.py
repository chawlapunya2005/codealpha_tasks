from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('projects/<int:project_pk>/tasks/create/', views.create_task, name='create_task'),
    path('projects/<int:project_pk>/members/add/', views.add_member, name='add_member'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/status/', views.update_task_status, name='update_task_status'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'),
]
