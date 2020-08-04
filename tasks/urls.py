from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_tasks, name="show_tasks"),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
]
