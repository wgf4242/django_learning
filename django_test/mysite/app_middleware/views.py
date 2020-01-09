
class SetRemoteAddrFromForwardFor(object):
	def process_request(self, request):
		try:
			real_ip = request,META['HTTP_X_FORWARD_FOR']
		except Exception as e:
			raise Exception
		else:
			real_ip = real_ip.split(',')[0]
			request.META['REMOTE_ADDR'] = real_ip


class MyMiddle(object):
	def __init__(self):
		pass

	def process_request():
		pass

	def process_views():
		pass
	
	def process_response():
		pass

	def process_exception():
		pass