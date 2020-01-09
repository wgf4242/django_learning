from django.conf.urls import url
from .views import *

# forms/url
urlpatterns = [
	url(r'^contact/$', contact),
	url(r'^contact2/$', contact2),
	url(r'^comment/$', comment),
	url(r'^comment2/$', comment2),
	url(r'^date/$', date),
	url(r'^helptext/$', htcf),
	url(r'^mchoice/$', multiple_choice),
	url(r'^admindate/$', admin_date_test),
]