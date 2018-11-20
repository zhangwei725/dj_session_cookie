from django.conf.urls import url

from cookie01 import views

urlpatterns = [
    url('set/', views.cookie1),
    url('get/', views.cookie2),
    url('1/', views.session1),
]
