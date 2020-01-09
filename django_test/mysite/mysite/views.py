from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponse("Hello world")

def my_homepage_view(request):
	return HttpResponse("404 not found")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body><html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html =  "<html><body>In %s hours(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def hours_ahead2(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	t = get_template('hours_ahead.html')
	html = t.render(Context({'hour_offset': offset, 'next_time': dt}))
	return HttpResponse(html)


def current_datetime_byfile(request):
	now = datetime.datetime.now()
	fp = open('C:/templates/mytemplates.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)


def current_datetime_bytemplate(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)


def current_datetime_bytemplate(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})

def current_datetime_bylocal(request):
	current_date = datetime.datetime.now()
	return render_to_response('current_datetime.html', locals())


from django.shortcuts import render_to_response
import MySQLdb

def book_list(request):
	
	db = MySQLdb.connect(user='root', db='test', passwd='', host='localhost')
	cursor = db.cursor()
	
	create_table_sql = "CREATE TABLE IF NOT EXISTS books ( \
			id int(10) AUTO_INCREMENT PRIMARY KEY, \
		    name varchar(20)) \
		    CHARACTER SET utf8"

	insert_sql = "INSERT INTO books(name) VALUES ('DjangoBook'), ('Head First')"


	try:
		cursor.execute("DROP TABLE IF EXISTS books")
		cursor.execute(create_table_sql)
		cursor.execute(insert_sql)

		cursor.execute('SELECT name FROM books ORDER BY name')
		names = [row[0] for row in cursor.fetchall()]
	except Exception as e:
		raise
	
	cursor.close()
	db.commit()
	db.close()
	return render_to_response('book_list.html', {'names': names})

from django.shortcuts import render_to_response

# from mysite.books.models 
# import Book

# def book_list(request):
# 	books = Book.objects.order_by('name')
# 	return render_to_response('book_list.html', {'books': books})


def ua_display_good2(request):
	ua = request.META.get('HTTP_USER_AGENT', 'unknown')
	return HttpResponse("Your browser is %s" % ua)

def display_meta(request):
	values = request.META.items()
	values = sorted(values)
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))