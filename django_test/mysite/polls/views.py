from django.http import HttpResponse
from django.template import loader,Context, RequestContext
from django.shortcuts import render_to_response
def hello(request):
	return HttpResponse("This is hello in polls.")

def page(request, num="1"):
    # Output the appropriate page of blog entries, according to num.
	return HttpResponse("num is %s ." % num )

# RequestContext and Context Processors

def view_1(request):
	# ...
	t = loader.get_template('template1.html')
	c = Context({
	'app': 'My app',
	# 'user': request.user,
	'ip_address': request.META['REMOTE_ADDR'],
	'message': 'I am view 1.'
	})
	return HttpResponse(t.render(c))

def view_2(request):
	# ...
	t = loader.get_template('template2.html')
	c = Context({
	'app': 'My app',
	# 'user': request.user,
	'ip_address': request.META['REMOTE_ADDR'],
	'message': 'I am the second view.'
	})
	return t.render(c)

def custom_proc(request):
	# "A context processor that provides 'app', 'user' and 'ip_address'."
	return {
	'app': 'My app',
	# 'user': request.user,
	'ip_address': request.META['REMOTE_ADDR']
	}
def rview_1(request):
	# ...
	t = loader.get_template('template1.html')
	c = RequestContext(request, {'message': 'I am view 1.'},
	processors=[custom_proc])
	return t.render(c)
def rview_2(request):
	# ...
	t = loader.get_template('template2.html')
	c = RequestContext(request, {'message': 'I am the second view.'},
	processors=[custom_proc])
	return t.render(c)


def my1(request):
	t = loader.get_template('template1.html')
	c = Context({
	'data': '3 < 2',
	})
	return HttpResponse(t.render(c))


def foo(request, template_name):
	# m_list =  Book.objects.all()
	m_list = ['a', 'b', 'c']
	print(template_name)
	return render_to_response(template_name, {'m_list' : m_list})
	

def views1(request):
	if 'a':
		#do...
		return
	return

def views2(request):
	if 'a':
		#do...
		return
	return	

def request_login(view):
	def new_view(request):
		#dosomething
		return view(request)
	return new_view


from django.template import Template
def article_detail(request, year, month, day):
	t = Template("<html><body>It is {{ year }}, {{month}}, {{day}} .</body></html>")
	html = t.render(Context({ 'year' : year ,'month' : month ,'day' : day }))
	return HttpResponse(html)