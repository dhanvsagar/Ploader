from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('upload', views.img_upload, name='upload'),
    path('about', views.about, name='about')

]
