# This is called the "app factory".
# I called it core.py, but it can be whatever you wish.
# Be creative. :)
from flask import Flask
from werkzeug.utils import find_modules, import_string

from myapp.api_helpers import ApiException

def create_app(config=None):
    app = ApiFlask(__name__)
    app.config.update(config or {})
    register_blueprints(app)
    register_other_things(app)
    register_error_handlers(app)
    return app

class ApiFlask(Flask):
    """Response Converter"""
    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)

def register_blueprints(app):
    """Automagically register all blueprint packages

    Just take a look in the blueprints directory.
    """
    for name in find_modules('myapp.blueprints', include_packages=True):
        mod = import_string(name)
        if hasattr(mod, 'blueprint'):
            app.register_blueprint(mod.blueprint)
    return None

def register_other_things(app):
    """e.g. extensions"""
    return None

def register_error_handlers(app):
    """Error Handler"""
    app.register_error_handler(ApiException, lambda err: err.to_result())
    return None


class MyThing(object):
    """Optional contained app

    Not exactly sure what this is for :)
    """
    def __init__(self, config):
        self.flask_app = create_app(config)
        self.flask_app.my_thing = self

    def __call__(self, environ, start_response):
        return self.flask_app(environ, start_response)


