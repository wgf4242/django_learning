"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.views import *
from books import views 
from paging import views as pagingview


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]



urlpatterns += [
    url(r'^hello/', hello),
    url(r'^$', my_homepage_view),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # url(r'^time/1/$', current_datetime_byfile),
    url(r'^time/2/$', current_datetime_bytemplate),
    url(r'^time/local/$', current_datetime_bylocal),
    url(r'^time/ha2/(\d{1,2})/$', hours_ahead2),
    url(r'^booklist/$', book_list),
    url(r'^ua/$', ua_display_good2),
    url(r'^dm/$', display_meta),
    url(r'^search_form/$', views.search_form),
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', my_homepage_view),
    url(r'^search/$', views.search),
    url(r'^addbook/$', views.addbook),
    url(r'^pindex/(\d*)', pagingview.index),
    url(r'^pinit/$', pagingview.test),
]



from django.conf.urls import *
from polls import views
urlpatterns += [
    url(r'^polls/', include('polls.urls')),
]

urlpatterns += [
    url(r'foo/$', views.foo, {'template_name' : 'template1.html'}),
    url(r'foo2/$', views.foo, {'template_name' : 'template2.html'}),

    url(r'views1/$', views.request_login(views.views1)),
    url(r'views2/$', views.request_login(views.views2)),
]

# books url
import books.views
urlpatterns += [
    url(r'^books/views/$', books.views.views)
]

urlpatterns += [
    url(r'^app_template/', include('app_template.urls')),
]

urlpatterns += [
    url(r'^app_generic_view/', include('app_generic_view.urls',namespace='generic_view')),
]

import django
urlpatterns += [
    url(r'^forms/', include('app_form.urls')),
    # url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict), 
    url(r'^jsi18n/$', django.views.i18n.javascript_catalog, name='jsi18n'),
]


import app_restFramework.views
from django.views.generic import TemplateView

class BookbaseView(TemplateView):

    template_name = "app_restFramework_form.html"

import app_restFramework.views

urlpatterns += [
    url(r'^app_restFramework/book_list', app_restFramework.views.book_list),
    url(r'^app_restFramework/book_form/$',  BookbaseView.as_view()),
    url(r'^app_restFramework/users/$', app_restFramework.views.UserList.as_view() ), 
    url(r'^app_restFramework/users/(?P<pk>[0-9]+)/$', app_restFramework.views.UserDetail.as_view() ), 
]

from app_restFramework.myView import api_root
urlpatterns += [
    url(r'^app_restFramework/$', api_root),
]

from myformset.views import manage_articles
urlpatterns += [
    url(r'^manage_articles/', manage_articles),
]

import app_ajax.views

urlpatterns += [
    url(r'^app_ajax/index', app_ajax.views.index),
    url(r'^app_ajax/add', app_ajax.views.add, name='ajax_add'),
    url(r'^app_ajax/ajax_list', app_ajax.views.ajax_list, name='ajax_list'),
    url(r'^app_ajax/ajax_dict', app_ajax.views.ajax_dict, name='ajax_dict'),
    url(r'^app_ajax/ajax_url_to_json', app_ajax.views.ajax_url_to_json, name='ajax_url_to_json'),
]


# cbv urls 

from django.views.generic.base import TemplateView
from cbv_dashboard.views import DashboardTemplateView, MyView,\
                         BookDetail, BookListView, BookCreateView,\
                         BookUpdateView, BookDeleteView
urlpatterns += [
    url(r'^book/create$', BookCreateView.as_view(), name='book_create'),
    url(r'^book/$', BookListView.as_view(), name='book_list'),
    url(r'^book/(?P<slug>[-\w]+)/$', BookDetail.as_view(), name='book_detail'),
    url(r'^book/(?P<slug>[-\w]+)/update$', BookUpdateView.as_view(), name='book_update'),
    url(r'^book/(?P<slug>[-\w]+)/delete$', BookDeleteView.as_view(), name='book_delete'),
    # url(r'^book/(?P<slug>[-\w]+)/$', BookDetail.as_view(), name='book_detail'),
    url(r'^someview/$', MyView.as_view(template_name = 'about.html')),
    url(r'^about/$', DashboardTemplateView.as_view(template_name = 'about.html'), name='about'),
    url(r'^team/$', DashboardTemplateView.as_view(template_name = 'team.html'), name='team'),
    # url(r'^about/$', views.about, name='about'),
]

# include django_form_formsets
urlpatterns += [
    url(r'^formsets/', include('django_form_formsets.urls')),
]