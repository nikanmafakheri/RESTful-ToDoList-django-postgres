from django.urls import path
from . import views

urlpatterns = [
  path('',views.ApiOverView,name='home'),
  path('create/',views.CreatePost,name='create'),
  path('all/',views.ViewPost,name='View'),
]