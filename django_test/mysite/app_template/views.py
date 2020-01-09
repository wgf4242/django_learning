from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from django.template import loader, Context, RequestContext

def view_1(request):
	# ...
	t = loader.get_template('template1.html')
	c = Context({
		'app' : 'My app',
		'user' : request.user,
		'ip_address' : request.META['REMOTE_ADDR'],
		'message' : 'I im view 1 .',
		})
	return HttpResponse(t.render(c))

def view_2(request):
	# ...
	t = loader.get_template('template2.html')
	c = Context({
		'app' : 'My app',
		'user' : request.user,
		'ip_address' : request.META['REMOTE_ADDR'],
		'message' : 'I im view 2 .',
		})
	return HttpResponse(t.render(c))

# not work
def view_3(request):
	# ...
	params = {'app' : 'My app',
		'user' : request.user,
		'ip_address' : request.META['REMOTE_ADDR'],
	}
	# t = loader.get_template('template1.html')
	# c = RequestContext(request, {'message' : 'I am view3.'}, params)
	# return HttpResponse(t.render(c))

	return render(request, 'template1.html', params)