from django.conf.urls import *
from . import views
# app_name = 'polls'

urlpatterns = [
    url(r'^hello/$', views.hello),
]
