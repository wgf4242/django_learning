from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from paging import models
from paging import common,html_helper
from django.utils.safestring import mark_safe

# Create your views here.

# 分页查询
def index(request, page):
	
	page  = common.try_int(page, 1)
	
	count = models.Host.objects.all().count()

	pageObj = html_helper.PageInfo(page,count)

	# 使用 property 装饰器去掉方法的括号
	result = models.Host.objects.all()[pageObj.start:pageObj.end]
	pages = html_helper.Pager(page, pageObj.all_page_count)
	# result = models.Host.objects.all()[pageObj.start():pageObj.end()]
	# pages = html_helper.Pager(page, pageObj.all_page_count())

	ret = {'data' : result , 'count' : count , 'pages' : pages}
	return render_to_response('pindex.html', ret)

def test(request):
	
	for i in range(1,21):
		models.Host.objects.create(HostName='host' + str(i), IP = '1.1.1.' + str(i))
	return HttpResponse("Success")
