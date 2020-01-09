from django.views.decorators.cache import cache_page
# cache_page 装饰器 , 在 urls.py 里配置， 不是每个视图都需要缓存

# @cache_page(60 * 15)
@cache_control(private = True, max_age = 3660, must_revalidate = True) #must_revalidate 重新验证留下来的缓存
def views(request):
	pass

# views = cache_page(views, 60 * 15)	

# python manage.py shell
# from django.core.cache import cache
# cache.set('python', 111, 600)
# cache.get('python')
# cache.add('django', 111, 500)
# cache.get('django')
# cache.get_many(['python', 'django'])
