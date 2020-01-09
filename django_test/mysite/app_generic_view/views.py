from django.template import TemplateDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from books.models import *
from .forms import BookModelForm


#@login_required()
def post_model_update_view(request, id=None):
	obj = get_object_or_404(Book, id=id)
	form = BookModelForm(request.POST or None, instance=obj)
	context = {
		# 'object': obj,
		'form' : form,
	}
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		messages.success(request, "Updated a Book")
		return HttpResponseRedirect("/app_generic_view/{num}".format(num=obj.id))

	template_name  = "app_generic_view/update-view.html"
	return render(request, template_name, context)
	
#@login_required()
def post_model_create_view(request):
	# if request.method == 'POST':
	# 	# print(request.POST)
	# 	form = BookModelForm(request.POST)
	# 	if form.is_valid():
	# 		form.save(commit=False)
	# 		print(form.cleaned_data)
	
	form = BookModelForm(request.POST or None)
	context = {'form': form}

	if form.is_valid():
		obj = form.save(commit=False)
		#print(obj.title)
		obj.save()
		messages.success(request, "Created a new Book")
		context = {
			'form' : BookModelForm(),
		}
		# return HttpResponseRedirect("/blog/{num}".format(num=obj.id))

	template_name = 'app_generic_view/create-view.html'

	return render(request, template_name, context)

def post_model_delete_view(request, id=None):
	obj = get_object_or_404(Book, id=id)
	if request.method == 'POST':
		obj.delete()
		messages.success(request, "Book deleted")
		return HttpResponseRedirect("/app_generic_view")

	context = {'object': obj}
	template_name  = 'app_generic_view/delete-view.html'
	return render(request, template_name, context)
	
def post_model_detail_view(request, id=None):
	# try:
	# 	obj = Book.objects.get(id=1)
	# except Exception as e:
	# 	raise Http404

	# qs = Book.objects.filter(id=100)
	# obj = None
	# if not qs.exists():
	# 	raise Http404
	# else:
	# 	obj = qs.first()

	obj = get_object_or_404(Book, id=id)
	context = {'object': obj}
	template_name  = 'app_generic_view/detail-view.html'
	
	return render(request, template_name, context)
	

def post_model_list_view(request):
	# query = request.GET.["q"]
	# Python Dictionary get() get(key, default=None)
	query = request.GET.get("q", None)
	qs = Book.objects.all()
	if query is not None:
		qs = qs.filter(
			Q(title__icontains=query) |
			Q(publisher__name__icontains=query)
			# Q(slug__icontains=query) 
			)

	context = {'object_list': qs}
	template_name = 'app_generic_view/list-view.html'

	return render(request, template_name, context)

# or set LOGIN_URL in settings.py
@login_required(login_url='/login/')
def login_required_view(request):
	print(request.user)
	qs = Book.objects.all()
	context = {'object_list': qs}

	if request.user.is_authenticated():
		template_name = 'app_generic_view/list-view.html'
	else:
		template_name = 'app_generic_view/list-public-view.html'
		# raise Http404
		return HttpResponseRedirect("/login")
	
	return render(request, template_name, context)

	# 'some_dict' : {"abc" : 123},
	# 'num': 123,
	# 'array_list': [123, 456, 789],


# def books_by_publisher(request, name):
# 	publisher = get_object_or_404(Publisher, name=name)
# 	print(publisher)
# 	return ListView.as_view(queryset=Book.objects.filter(publisher=publisher),
#         template_name='publisher_list_page.html')(request)
	# return ListView.as_view(queryset=Book.objects.filter(publisher=publisher),
	        # template_name='publisher_list_page.html')(request)
	# return ListView.as_view(request, queryset=Book.objects.filter(publisher=publisher),
	# 	template_name='publisher_list_page.html')
    	# template_name='publisher_list_page.html', template_objects_name = 'book',)

def views(request):
	try:
		return TemplateView.as_view(request, template = "about/%s.html" % page)
	except TemplateDoesNotExist:
		raise Http404()

def about(request, word):
	return HttpResponse("done, request word is %s " % word)


def post_model_robust_view(request,id=None):
	
	obj = None
	context = {}
	success_message = 'A new book was created'
	
	if id is not None:
		"obj is could be created"
		template_name = "app_generic_view/create-view.html"
	else:
		"obj is could be exists"
		obj = get_object_or_404(Book, id=id)
		success_message = 'A new book was created'
		context['object']= obj
		template_name = "app_generic_view/detail-view"
		if "edit" in request.get_full_path():
			template_name  = "app_generic_view/update-view.html"
		if "delete" in request.get_full_path():
			template_name = "app_generic_view/delete-view.html"
			if request.method == 'POST':
				obj.delete()
				messages.success(request, "Book deleted")
				return HttpResponseRedirect("/app_generic_view")


	# if "edit" in request.get_full_path() or "create" in request.get_full_path():
	form = BookModelForm(request.POST or None, instance=obj)
	context["form"] = form
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		messages.success(request,success_message)
		if obj is not None:
			return HttpResponseRedirect("/app_generic_view/{num}".format(num=obj.id))

		context["form"] = BookModelForm()
	return render(request, tempalte_name, context)			
