from django.conf.urls import url
from django_form_formsets import views

# /formsets/home

urlpatterns = [
    url(r'^home/', views.home),
    url(r'^formset/', views.formset_view),
]