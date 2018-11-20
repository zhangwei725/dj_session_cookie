from django.conf.urls import url, include
from django.contrib import admin

from account import views

urlpatterns = [
    url('login/', views.login, name='login'),
    url('register/', views.register, name='register'),
    url('list/', views.list, name='list')
]
