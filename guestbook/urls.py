from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('upload', views.upload, name='upload'),
    path('about', views.about, name='about'),
]
