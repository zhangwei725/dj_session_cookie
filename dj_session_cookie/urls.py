from django.conf.urls import url, include
from django.contrib import admin

from account import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.index),
    url('cookie/', include('cookie01.urls')),
    url('account/', include('account.urls')),
]
