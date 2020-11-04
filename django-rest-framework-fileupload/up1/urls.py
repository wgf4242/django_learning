from django.conf.urls import url
from django.urls import re_path

from up1.views import FileUploadView, ExampleView, ExampleExcelView, FileUploadDefaultView
from .views import FileView

urlpatterns = [
    re_path(r'^upload/$', FileView.as_view(), name='file-upload'),
    re_path(r'^upload1/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    re_path(r'^upload2/$', ExampleView.as_view()),
    re_path(r'^upload3/$', FileUploadDefaultView.as_view()),
    re_path(r'^upload_excel/$', ExampleExcelView.as_view()),
]
