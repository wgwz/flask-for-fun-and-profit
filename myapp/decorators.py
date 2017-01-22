from functools import update_wrapper
from flask import request
from voluptuous import Invalid

from myapp.api_helpers import ApiException

def dataschema(schema):
    def decorator(f):
        def new_func(*args, **kwargs):
            try:
                kwargs.update(schema(request.get_json()))
            except Invalid as e:
                raise ApiException(
                    'Invalid data: %s (path "%s")' %
                    (e.msg, '.'.join(e.path))
                )
            return f(*args,**kwargs)
        return update_wrapper(new_func, f)
    return decorator