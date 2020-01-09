from django.shortcuts import render_to_response,render
from django.http import HttpResponse

# Create your views here.
from books.forms import BookForm


def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)

# BAD!
def bad_search(request):
# The following line will raise KeyError if 'q' hasn't
# been submitted!
	message = 'You searched for: %r' % request.GET['q']
	return HttpResponse(message)

from books.models import Book
# def search(request):
# 	if 'q' in request.GET and request.GET['q']:
# 		q = request.GET['q']
# 		books = Book.objects.filter(title__icontains=q)
# 		# The icontains is a lookup type (as explained in Chapter 5 and Appendix B),
# 		return render_to_response('search_results.html', {'books': books, 'query': q})
# 	else:
# 		return render_to_response('search_form.html', {'error': True})

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html', {'books': books, 'query': q})
	return render_to_response('search_form.html', {'errors': errors})

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Enter a subject.')
		if not request.POST.get('message', ''):
			errors.append('Enter a message.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid email address.')
		if not errors:
			# send_mail(
			# request.POST['subject'],
			# request.POST['message'],
			# request.POST.get('email', 'noreply@example.com'),
			# ['siteowner@example.com'],
			# )
			return HttpResponseRedirect('/contact/thanks/')
	return render_to_response('contact_form.html',
		{'errors': errors})


from django.shortcuts import render_to_response,render
from django.http import HttpResponse

def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Enter a subject.')
		if not request.POST.get('message', ''):
			errors.append('Enter a message.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid email address.')
		if not errors:
			# send_mail(
			# request.POST['subject'],
			# request.POST['message'],
			# request.POST.get('email', 'noreply@example.com'),
			# ['siteowner@example.com'],
			# )
			return HttpResponseRedirect('/contact/thanks/')
	return render(request, 'contact_form.html', {
		'errors': errors,
		'subject': request.POST.get('subject', ''),
		'message': request.POST.get('message', ''),
		'email': request.POST.get('email', ''), 
		})

from django.shortcuts import render_to_response
from books.forms import ContactForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm()
	return render(request, 'contact_form.html', {'form': form})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
		initial={'subject': 'I love your site!'}
		)
	return render(request, 'contact_form.html', {'form': form})

def	 addbook(request):
	# 使用 django Form的情况
	# book_form = BookForm(request.POST)
	# if book_form.is_valid():
	# 	book_form.objects.create(
	# 		title = book_form.cleaned_data['title'],
	# 		author = book_form.cleaned_data['author'],
	# 		publisher = book_form.cleaned_data['publisher'],
	# 		publication_date = book_form.cleaned_data['publication_date'],
	# 		)

	# 使用 django ModelForm的情况
	book_form = BookForm(request.POST)
	if book_form.is_valid():
		book_form.save()
		return HttpResponse("添加成功")
	else:
		book_form = BookForm()
	return render(request, "mybooks.html", {'form': book_form})
	# return render(request, "mybooks.html", locals())

def view_book(request):
	# b = Book.objects.get(id = 1)
	# b.publisher
	
	p = Publisher.objects.get(name = 'python')
	p.book_set.all()
	p.book_set.filter(name__icontains = 'django')

	a = Authors.objects.get(id = 1)
	a.book_set.all()
	# a.book_set.filter(xxx condition)

def views(request):
	# 获取名为 django 书的数量
	n = Book.objects.get_title('django')
	# 获取名为 django 书的对象
	b = Book.objects.all()
	print(b)

	Book.python_objects.filter()
	print(Book.python_objects.filter())

	return HttpResponse("Success")