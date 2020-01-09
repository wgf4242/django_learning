from django.conf.urls import *
# from app_template.views import *
# app_template.views abbrev for .views 
from .views import *


urlpatterns = [
    url(r'^view1/$', view_1),
    url(r'^view3/$', view_3),
    # url(r'^view2/)', view2),
]