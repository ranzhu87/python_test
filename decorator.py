def log(text):
	if isinstance(text,str) :
	    def decorator(func):
	        @functools.wraps(func)
	        def wrapper(*args, **kw):
	            print '%s %s():' % (text, func.__name__)
	            return func(*args, **kw)
	        return wrapper
	    return decorator
	else:
		@functools.wraps(text)
	        def wrapper(*args, **kw):
	            print '%s %s():' % ('call', text.__name__)
	            return text(*args, **kw)
	        return wrapper
