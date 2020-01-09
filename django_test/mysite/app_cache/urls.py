from django.conf.urls import url
from .views import * 
from django.views.decorators.cache import cache_page

urlpatterns = [
	url(r'views/$', cache_page(views, 60 * 15))
    

]