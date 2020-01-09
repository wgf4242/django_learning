from django.shortcuts import render_to_response
from django.http import HttpResponse
from app_form.forms import *

def contact(request):
	if request.method == 'POST' :
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			subject = cd['subject']
			message = cd['message']
			email = cd['email']
		else:
			form = ContactForm()
			initial={'subject':'hello world'}
			return render_to_response('login.html', {'form' : form})

def contact2(request):
	form = ContactForm2(label_suffix='?')
	return HttpResponse(form.as_p())

def comment(request):
	form = CommentForm(auto_id=False)
	return HttpResponse(form.as_p())

def comment2(request):
	default_data = {'name': 'Your name', 'url': 'http://'}
	# This trigger validation, all errors will display
	form = CommentForm(default_data,auto_id=False)
	return HttpResponse(form.as_p())

def date(request):
	form = DateForm()
	return HttpResponse(form.as_p())

def htcf(request):
	form = HelpTextContactForm(auto_id=False)
	return HttpResponse(form.as_p())

def multiple_choice(request): 
	form = MultipleChoiceForm()
	# return HttpResponse('<form action="">' +form.as_p() + '<input type="submit" value="Submit"> </form>')
	return render_to_response('form_test.html', {'form':form})

def admin_date_test(request): 
	form = AdminDateForm()
	return render_to_response('form_test.html', {'form':form})

