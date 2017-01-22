from flask import url_for, request
from voluptuous import Schema, REMOVE_EXTRA

from myapp.api_helpers import ApiException, ApiResult
from myapp.decorators import dataschema
from . import blueprint

@blueprint.route('/')
def index():
    return url_for('core.index', _external=True)

@blueprint.route('/add')
def add_numbers():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        raise ApiException('Numbers must be integers')
    return ApiResult({'result': a + b})

@blueprint.route('/subtract', methods=['POST'])
@dataschema(Schema({
    'a': int,
    'b': int
}, extra=REMOVE_EXTRA))
def sub_numbers(a, b):
    return ApiResult({'diff': a - b})