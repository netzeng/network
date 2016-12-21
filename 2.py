def deco(func):
	def _deco(a,b):
		print("before myfunc() called.")
		ret=func(a,b)
		print("after myfunc() called %s" % ret)
		return ret
	return _deco

@deco
def myfunc(a,b):
	print("myfunc(%s,%s)called."%(a,b))
	return a+b

myfunc(1,2)