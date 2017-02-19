from functools import update_wrapper
from flask import request
from voluptuous import Invalid

from myapp.api_utils import ApiResult, ApiException

def dataschema(schema):
    def decorator(f):
        def new_func(*args, **kwargs):
            try:
                kwargs.update(schema(request.get_json()))
            except Invalid as e:
                raise ApiException(
                    "Invalid data: %s (path '%s')" % (e.msg, '.'.join([str(v) for v in e.path]))
                )
            return f(*args,**kwargs)
        return update_wrapper(new_func, f)
    return decorator

def apiresult(f):
    def new_func(*args, **kwargs):
        rv = f(*args, **kwargs)
        return ApiResult(rv)
    return update_wrapper(new_func, f)
