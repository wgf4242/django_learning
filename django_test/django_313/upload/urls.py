from django.urls import path

from upload.views import upload0
from django_313.urls import urlpatterns

urlpatterns = [
    path('view0', upload0)
]
