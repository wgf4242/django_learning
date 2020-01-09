class MyMiddleWare(object):
	def __init__(self, get_response):	#只执行一次
	    self.get_response = get_response
	    print('My Middleware init')

	def __call__(self, request):
	    # Code to be executed for each request before
	    # the view (and later middleware) are called.
	    print('My Middleware request')
	    response = self.get_response(request)

	    # Code to be executed for each request/response after
	    # the view is called.
	    return response
