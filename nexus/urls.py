from django.contrib import admin
from django.urls import path
from nexus import views
urlpatterns = [
    path('', views.index,name='home'),
    path('projects/' , views.projects,name='projects'),
    path('register/' , views.register,name='register')
]
