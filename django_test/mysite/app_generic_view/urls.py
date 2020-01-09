from django.conf.urls import *
from django.views.generic import TemplateView
from django.views.generic import ListView

from app_generic_view.views import *
from books.models import *

def find_book():
	return Book.objects.all()

class PublisherView(ListView):
    model = Publisher
    template_name = 'publisher_list_page.html'
    # next line is deault if ommit , comment this line is same with not comment
    queryset=Publisher.objects.all()
    # queryset=Publisher.objects.filter(name='test')

class PublisherBookListView(ListView):

	context_object_name = "publisher_list"
	template_name = "publisher_list_page.html"

	def get_queryset(self):
		publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
		return Book.objects.filter(publisher=publisher)

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),    
    url(r'^about/(\w+)/$', about),    
    url(r'^publisher/$', PublisherView.as_view()),
    url(r'^publisher1/$', ListView.as_view(queryset=Publisher.objects.all(),
    	template_name='publisher_list_page.html')),
    url(r'^publisher2/$', ListView.as_view(model=Publisher,
    	template_name='publisher_list_page.html',context_object_name = 'publisher_list')),
    # app_generic_view/books/test,  need a publisher named 'test'
    url(r'^books/(\w+)/$', PublisherBookListView.as_view()),
    # url(r'^books1/(\w+)/$', books_by_publisher),
    url(r'^$', post_model_list_view, name='list'),
    url(r'^(?P<id>\d+)$', post_model_detail_view, name='detail'),
    url(r'^(?P<id>\d+)/delete$', post_model_delete_view, name='delete'),
    url(r'^create$', post_model_create_view, name='create'),
    url(r'^(?P<id>\d+)/edit$', post_model_update_view, name='update'),
]