from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/accept/', views.accept_project, name='accept_project'),
    path('tasks/<int:task_id>/update/', views.update_task_status, name='update_task_status'),
    path('projects/<int:pk>/progress/', views.project_progress, name='project_progress'),
]
