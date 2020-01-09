
def try_int(arg, default):
	ret = None
	try:
		arg = int(arg)
	except Exception as e:
		arg = default

	return arg
	

	