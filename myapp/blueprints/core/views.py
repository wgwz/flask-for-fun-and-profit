from flask import url_for, request, Blueprint
from flask.views import MethodView
from voluptuous import Schema, REMOVE_EXTRA, Required

from myapp.api_utils import ApiException
from myapp.decorators import dataschema, apiresult

bp = Blueprint('core', __name__, url_prefix='/v1.0')

@bp.route('/')
@apiresult
def index():
    return url_for('core.index', _external=True)

@bp.route('/sum')
@apiresult
def sum():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        raise ApiException('Numbers must be integers')
    return {'result': a + b}


schema = Schema({
    Required('a'): int,
    Required('b'): int
}, extra=REMOVE_EXTRA)

@bp.route('/difference', methods=['POST'])
@apiresult
@dataschema(schema)
def difference(a, b):
    return {'difference': a - b}

class DifferenceApi(MethodView):

    @apiresult
    @dataschema(schema)
    def post(self, a, b):
        return {'difference': a - b}

bp.add_url_rule('/subtract', view_func=DifferenceApi.as_view('difference_method_view'))