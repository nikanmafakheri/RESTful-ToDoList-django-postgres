from django.urls import path
from . import views

urlpatterns = [
  path('',views.ApiOverView,name='home'),
  path('task/',views.CreateTask,name='create'),
  path('tasks/',views.ViewTask,name='view'),
  path('task/<int:pk>/',views.TaskOperation,name='operation'),
  # path('task/<int:pk>/',views.TaskOperation,name='delete'),
]