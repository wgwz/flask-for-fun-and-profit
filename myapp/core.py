# This is called the "app factory".
from werkzeug.utils import find_modules, import_string

from myapp.api_utils import ApiFlask, ApiException

def create_app(config=None):
    app = ApiFlask(__name__)
    app.config.update(config or {})
    register_blueprints(app)
    register_other_things(app)
    register_error_handlers(app)
    return app

def register_blueprints(app):
    """Automagically register all blueprint packages

    Just take a look in the blueprints directory.
    """
    for name in find_modules('myapp.blueprints', recursive=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None

def register_other_things(app):
    """e.g. extensions"""
    return None

def register_url_rules(app):
    """eventually come up with a way"""
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


